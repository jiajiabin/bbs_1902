from flask import (
    Blueprint,
    render_template,
    request,
    g,
session
)
from .models import Front_User_Article
from ..front.decorators import login_required
from apps.front.models import FrontUser
from exts import db
# 前台页面的本bp
bp = Blueprint("msg",__name__,url_prefix='/msg')

# 发帖页面
username = ""
@bp.route('/post_msg/',endpoint='post_msg',methods=['POST','GET'])
@login_required
def post_msg():
    global username
    if request.method == "GET":
        import config
        user = FrontUser.query.get(session[config.Front_USER_ID])
        username = user.username

        content ="人生苦短 我学python"
        return render_template("message/post_message.html", content=content)
    else:
        print(username)
        content=request.form.get("content")
        title = request.form.get("title")
        # 字符串切割 把左右两边的p标签切割掉  留下纯文本text
        text = content[3:-4]
        print(text,title)

        article = Front_User_Article(title=title,data_text=text)

        user = FrontUser.query.filter_by(username=username).first()
        # article.articles.append(user)
        user.articles.append(article)
        db.session.add(user)
        db.session.commit()
        return ""
