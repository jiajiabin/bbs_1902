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

ACCESS_KEY = "uYM5IH5gOKDBTq2I_iGJxdKD-_j_EcMXEYLoDk4j"
SECRET_KEY = "JVwLgSrcLIES4Tu5dZ5zN2a0oAy_X08H_cUakieP"
BUCKET_NAME = "jiajiabin"
DOMAIN = "http://py645ayfc.bkt.clouddn.com/"

# 富文本编辑器 ueditor 的配置文件
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'ufiles')
# 先注释其中的七牛云配置
# UEDITOR_UPLOAD_TO_QINIU = True
# UEDITOR_QINIU_ACCESS_KEY = ACCESS_KEY
# UEDITOR_QINIU_SECRET_KEY = SECRET_KEY
# UEDITOR_QINIU_BUCKET_NAME = BUCKET_NAME"
# UEDITOR_QINIU_DOMAIN = "http://py645ayfc.bkt.clouddn.com"

