# encoding:utf-8
import os

SECRET_KEY = os.urandom(24)

# 绑定数据库
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'bbs'
USERNAME = 'root'
PASSWORD = 'hujiabin1'
DB_UI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                       password=PASSWORD, host=HOSTNAME,
                                                                                       port=PORT, db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_UI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 初始定义，每次用户得到session重新赋值
CMS_USER_ID = 'ASDFSADFDSFSDFSDF'
Front_USER_ID = 'ASDFSADFDSFSDFSDF'
