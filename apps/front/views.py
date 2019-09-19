from flask import (
    Blueprint,
    render_template,
    g
)

# 前台页面的本bp
bp = Blueprint("home",__name__,url_prefix='/home')

# 前台主页
@bp.route('/',endpoint='index')
def index():
    content = {
        "user_id":""
    }
    # if g.username:
    #     user_id = g.username
    return render_template('front/front_index.html', content=content)

