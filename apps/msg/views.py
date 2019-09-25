from flask import (
    Blueprint,
    render_template,
    request,
)
from ..front.decorators import login_required

# 前台页面的本bp
bp = Blueprint("msg",__name__,url_prefix='/msg')

# 发帖页面
@bp.route('/post_msg/',endpoint='post_msg',methods=['POST','GET'])
@login_required
def post_msg():
    if request.method=="POST":
        content=request.form.get("content")
        # 字符串切割 把左右两边的p标签切割掉  留下纯文本text
        text = content[3:-4]
        print(text)
        return ""
    else:
        content ="人生苦短 我学python"
        return render_template("message/post_message.html", content=content)
