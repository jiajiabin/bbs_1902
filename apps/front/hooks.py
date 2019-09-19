from .views import bp
import config
from flask import session,g
from .models import FrontUser

# 钩子函数
@bp.before_request
def before_request():
    if config.Front_USER_ID in session:
        user_id = session.get(config.Front_USER_ID)
        # 通过ID在数据库查找用户对应的模型对象
        front_user = FrontUser.query.get(user_id)
        if front_user:
            g.cms_user = front_user
    # 未登录则默认游客登录
    else:
        g.cms_user = None