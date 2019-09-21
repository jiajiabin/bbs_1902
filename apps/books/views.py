from flask import (
    Blueprint,
    render_template,
)



# 图书页面的本bp
bp = Blueprint("book",__name__,url_prefix='/book')

# 前台主页
@bp.route('/',endpoint='index')
def index():
    content = {
        "user_id":None
    }
    return render_template('books/boos_index.html', content=content)