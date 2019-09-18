from .views import bp
import config
from flask import session,g
from .models import CMSUser

# 钩子函数
@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        # 通过ID在数据库查找用户对应的模型对象
        cms_user = CMSUser.query.get(user_id)
        if cms_user:
            g.cms_user = cms_user