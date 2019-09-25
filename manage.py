from flask_script import Manager
from bbs import create_app
from apps.cms import models as cms_models
from apps.books import models as books_models
from flask_migrate import Migrate,MigrateCommand
from exts import db
import requests
import json


# 绑定后台的数据，数据库模板
CMSUser = cms_models.CMSUser
# 绑定app
app = create_app()
manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)

# 命令行存入数据
@manager.option('-u','--username',dest="username")
@manager.option('-p','--password',dest="password")
@manager.option('-e','--email',dest="email")
def create_cms_user(username,password,email):
    user = CMSUser(username=username,password=password,email=email)
    db.session.add(user)
    db.session.commit()
    print("cms用户添加成功")
# 命令行生成管理员账号
# python manage.py create_cms_user -u 123456 -p 123456 -e 123456@qq.com

# 上传图书用于测试
@manager.command
def create_test_post():
    Books = books_models.Books
    Author = books_models.Author
    author = Author.query.filter_by(authorname="jiabin").first()
    for x in range(1,200):
        title = "标题:%s" %x
        text = "内容:%s" %x
        book = Books(bookname=title,text=text)
        author.bookes.append(book)
        db.session.add(author)
        db.session.commit()
    print("图书添加成功")

# 用于天气预报测试
@manager.command
def weather_test():
    response = requests.get("http://api.asilu.com/weather/?city=beijin")
    response.raise_for_status()
    weather_data = json.loads(response.text)
    print(weather_data)
# {'city': '北京', 'pm25': '75', 'weather': [{'date': '周三 09月25日', 'icon1': 'day/qing', 'icon2': 'night/qing', 'weath
# er': '晴', 'wind': '南风微风', 'temp': '31 ~ 15℃'}, {'date': '周四', 'icon1': 'day/qing', 'icon2': 'night/qing', 'weat
# her': '晴', 'wind': '东南风微风', 'temp': '30 ~ 15℃'}, {'date': '周五', 'icon1': 'day/duoyun', 'icon2': 'night/duoyun'
# , 'weather': '多云', 'wind': '南风微风', 'temp': '29 ~ 15℃'}, {'date': '周六', 'icon1': 'day/qing', 'icon2': 'night/du
# oyun', 'weather': '晴转多云', 'wind': '西南风微风', 'temp': '29 ~ 17℃'}], 'date': '2019-09-25', 'id': '101010100', 't'
# : 1569340800}


if __name__ == "__main__":
    manager.run()