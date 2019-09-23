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

ACCESS_KEY = '9cfPzRDY3ZzJTKb1jz1WqR_v3xWfJDxzx7AAq-sx'
SECRET_KEY = 'WpdY-0OArlfFHg39729m-TZzvzP-xUjPbrVn6h5N'
BUCKET_NAME = "jiajiabin1"
DOMAIN = "http://py9kh9odc.bkt.clouddn.com/"

# 富文本编辑器 ueditor 的配置文件
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'ufiles')
# 先注释其中的七牛云配置
# UEDITOR_UPLOAD_TO_QINIU = True
# UEDITOR_QINIU_ACCESS_KEY = ACCESS_KEY
# UEDITOR_QINIU_SECRET_KEY = SECRET_KEY
# UEDITOR_QINIU_BUCKET_NAME = BUCKET_NAME"
# UEDITOR_QINIU_DOMAIN = "http://py645ayfc.bkt.clouddn.com"

