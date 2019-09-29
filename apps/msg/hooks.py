from .views import bp
import config
from flask import session,g
from apps.front.models import FrontUser
from flask import g
from ..front.hooks import front_user

@bp.before_request
def before_request():
    g.front_user = front_user

# 钩子函数
@bp.before_request
def before_request():
    if config.Front_USER_ID in session:
        user_id = session.get(config.Front_USER_ID)
        # 通过ID在数据库查找用户对应的模型对象
        front_user = FrontUser.query.get(user_id)
        if front_user:
            g.front_user = front_user
        else:
            g.front_user = ""
    # 未登录则默认游客登录
    else:
        g.front_user = None