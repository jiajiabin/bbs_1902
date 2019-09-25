from .views import bp
from flask import g
from ..front.hooks import front_user

@bp.before_request
def before_request():
    g.front_user = front_user