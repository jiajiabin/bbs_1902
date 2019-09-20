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

# 富文本编辑器 ueditor 的配置文件
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'ufiles')
# 先注释其中的七牛云配置
# UEDITOR_UPLOAD_TO_QINIU = True
# UEDITOR_QINIU_ACCESS_KEY = "p_p2-jutlTI1mlPCSfMEO8DyZnkQaiFrd9IOlvpz"
# UEDITOR_QINIU_SECRET_KEY = "rN0YQux570vbhL5d8QvShrV-SnjzTdqhlfWstWri"
# UEDITOR_QINIU_BUCKET_NAME = "bbs1902"
# UEDITOR_QINIU_DOMAIN = "http://pxwhlyank.bkt.clouddn.com/"
