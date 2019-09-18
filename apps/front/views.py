from flask import Blueprint,render_template

# 前台页面的蓝本bp
bp = Blueprint("home",__name__,url_prefix='/home')

# 前台主页
@bp.route('/',endpoint='index')
def index():
    return render_template('front/index.html')