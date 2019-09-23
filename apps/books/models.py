from exts import db
from datetime import datetime

# 绑定图书数据，数据库模板
class Books(db.Model):
    # 数据库存储数据
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    bookname = db.Column(db.String(50), nullable=False, unique=True)
    # author = db.Column(db.String())
    score = db.Column(db.Float, default=0)
    bookimg = db.Column(db.String(50))
    join_time = db.Column(db.DateTime, default=datetime.now)

author_books = db.Table(
    "author_books",
    db.Column("author_id",db.Integer,db.ForeignKey("author.id")),
    db.Column("books_id",db.Integer,db.ForeignKey("books.id"))
)

# 绑定图书的作者数据，数据库模板
class Author(db.Model):
    # 数据库存储数据
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    authorname = db.Column(db.String(20), nullable=False)
    # 作者简介允许为空
    author_about = db.Column(db.Text,default="")
    # 外链连接用户表，多对多
    bookes = db.relationship('Books',
                             secondary=author_books,
                             backref=db.backref('author', lazy='dynamic'))

books_tags = db.Table(
    "books_tags",
    db.Column("books_id",db.Integer,db.ForeignKey("books.id")),
    db.Column("tags_id",db.Integer,db.ForeignKey("tags.id"))
)

# 绑定图书的作者数据，数据库模板
class Tags(db.Model):
    # 数据库存储数据
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), default="其他")
    # 外链连接用户表，多对多
    bookes = db.relationship('Books',
                             secondary=books_tags,
                             backref=db.backref('tags', lazy='dynamic'))
