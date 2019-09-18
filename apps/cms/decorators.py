from flask import session,redirect,url_for
from functools import wraps
import config

# 装饰器，判断用户是否注册
def login_required(func):
    def inner(*args,**kwargs):
        if config.CMS_USER_ID in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('cms.login'))
    return inner