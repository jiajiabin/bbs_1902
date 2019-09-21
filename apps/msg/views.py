from flask import (
    Blueprint,
    render_template
)

# 前台页面的本bp
bp = Blueprint("msg",__name__,url_prefix='/msg')

# 发帖页面
@bp.route('/post_msg/',endpoint='post_msg')
def post_msg():
    return render_template('message/post_message.html')