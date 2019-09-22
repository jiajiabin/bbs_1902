from exts import db
from datetime import datetime

# 绑定图书数据，数据库模板
class Books(db.Model):
    # 数据库存储数据
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    bookname = db.Column(db.String(50), nullable=False, unique=True)
    # author = db.Column(db.String())
    score = db.Column(db.Float, nullable=False, unique=True)
    bookimg = db.Column(db.String(50), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)

# 绑定图书的作者数据，数据库模板
class Author(db.Model):
    # 数据库存储数据
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 通过作者id与图书关联，多对多，作者允许同名，不允许同id
    authorid = db.Column(db.Integer, nullable=False, unique=True)
    authorname = db.Column(db.String(20), unique=True)
    # 作者简介允许为空
    author_about = db.Column(db.Text)
    # 外链连接用户表，多对多
    # uid = db.Column(db.Integer,db.ForeignKey("front_user.id"))
    # article_author = db.relationship("FrontUser",backref="articles")