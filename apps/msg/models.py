from exts import db
from datetime import datetime

# 绑定前台的用户发帖数据，数据库模板
class Front_User_Article(db.Model):
    # 数据库存储数据
    __tablename__ = 'front_user_article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    data_text = db.Column(db.Text,nullable=False)
    post_time = db.Column(db.DateTime, default=datetime.now)
    # 外链连接用户表，1对多
    uid = db.Column(db.Integer,db.ForeignKey("front_user.id"))
    article_author = db.relationship("FrontUser",backref="articles")