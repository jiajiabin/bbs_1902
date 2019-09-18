from flask import (
    Blueprint,
    render_template,
    views
)
from ..front import bp as front_bp
from ..cms import bp as cms_bp


# 公共页面的蓝本bp
bp = Blueprint("common",__name__,url_prefix='/')

# 公共主页，类视图,用于用户跳转，主页介绍
class CommonView(views.MethodView):
    def get(self,message=None):
        return render_template('common/index.html',message=message)
bp.add_url_rule('/',view_func=CommonView.as_view('common'))

# 跳转论坛主页
class IndexView(views.MethodView):
    def get(self,message=None):
        return render_template('front/index.html',message=message)
front_bp.add_url_rule('/',view_func=IndexView.as_view('index1'))

# 跳转后台管理
class CmsView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/cms_login.html',message=message)
cms_bp.add_url_rule('/',view_func=CmsView.as_view('index1'))