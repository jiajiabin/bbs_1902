from flask import (
    Blueprint,
    render_template,
    request,
    g,
    session
)
from apps.msg.models import Front_User_Article, ArticleText
from ..front.decorators import login_required
from apps.front.models import FrontUser
from exts import db
from flask_paginate import Pagination, get_page_parameter
from config import PER_PAGE

# 前台页面的本bp
bp = Blueprint("msg", __name__, url_prefix='/msg')

# 发帖页面
username = ""


@bp.route('/post_msg/', endpoint='post_msg', methods=['POST', 'GET'])
@login_required
def post_msg():
    global username
    content = "人生苦短 我学python"
    if request.method == "GET":
        import config
        user = FrontUser.query.get(session[config.Front_USER_ID])
        username = user.username
        return render_template("message/post_message.html", content=content)
    else:
        content = request.form.get("content")
        title = request.form.get("title1")
        # 字符串切割 把左右两边的p标签切割掉  留下纯文本text
        text = content[3:-4]
        article = Front_User_Article(title=title)
        article_text = ArticleText(data_text=text)
        user = FrontUser.query.filter_by(username=username).first()
        article.texts = article_text
        db.session.add(article)
        user.articles.append(article)
        db.session.add(user)
        db.session.commit()

        return render_template("message/post_message.html", content=content)


@bp.route('/show_msg/', endpoint='show_msg', methods=['POST', 'GET'])
def index():
    page = request.args.get(get_page_parameter(), type=int, default=1)  # 从前端获取你要查看的页码
    # select * from posts limit start,总共多少条;
    start = (page - 1) * PER_PAGE  # 从哪里开始查询  索引值
    # 第几页 start end 每页显示条数
    # 1      0     9      10
    # 2      10    19     10
    end = start + PER_PAGE  # 在哪里结束    索引值
    # 表示从数据库中查出来的所有的帖子文章   每一页的
    posts = None
    # 所有文章的总数
    total = 0
    # 上一页 1 2... 48 49 50 51 52... 97 98下一页
    # 查出所有的贴子
    query_obj = Front_User_Article.query.order_by(Front_User_Article.post_time.desc())
    # 统计帖子的总数
    total = query_obj.count()
    # 相当于 select * from posts limit 1,2
    # 将查出来的帖子 切割到每一页
    posts = query_obj.slice(start, end)
    # 调用分页对象
    # bs_version bootstrap 样式版本 默认2
    # page 从前端传递过来的 用户想查看第几页
    # total 表示 帖子的总数
    # inner_window 当前页码的 左边 和右边 分别有几个页码
    # outer_window  上一页的右边    下一页的左边  有几个   0 代表有一个 如果你想显示5个  那么就是4

    pagination = Pagination(bs_version=3, page=page, total=total, inner_window=2, outer_window=0)
    context = {
        'pagination': pagination,
        'posts': posts
    }
    return render_template('message/show_message.html', **context)
