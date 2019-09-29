from exts import db
from datetime import datetime

# 绑定前台的用户发帖数据，数据库模板
class Front_User_Article(db.Model):
    # 数据库存储数据
    __tablename__ = 'front_user_article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    # data_text = db.Column(db.Text,nullable=False)
    post_time = db.Column(db.DateTime, default=datetime.now)
    # 外链连接用户表，1对多
    uid = db.Column(db.Integer,db.ForeignKey("front_user.id"))
    article_author = db.relationship("FrontUser",backref="articles")

# 帖子的详细内容，1对1额外模型
class ArticleText(db.Model):
    __tablename__ = 'articletext'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_text = db.Column(db.Text,nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey("front_user_article.id"))
    articles = db.relationship("Front_User_Article", backref=db.backref("texts", uselist=False))

# 绑定发帖的评论数据，数据库模板
class Article_Comment(db.Model):
    # 数据库存储数据
    __tablename__ = 'article_comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 发帖人name
    comment_name = db.Column(db.String(50), nullable=False)
    comment_text = db.Column(db.Text,nullable=False)
    post_time = db.Column(db.DateTime, default=datetime.now)
    # 外链连接帖子表，1对多
    uid1 = db.Column(db.Integer,db.ForeignKey("front_user_article.id"))
    articles = db.relationship("Front_User_Article",backref="comment")
    # 外链连接作者表，1对多
    uid2 = db.Column(db.Integer,db.ForeignKey("front_user.id"))
    authors = db.relationship("FrontUser",backref="authors_comment")