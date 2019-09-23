# -*-coding:utf-8 -*-
from flask import (
    Blueprint,
    render_template,
    views,
    g,
    request,
    session,
    url_for,
    redirect,
)
from .forms import LogUpForm,LoginForm
from .models import FrontUser
from exts import db
import config
from .decorators import login_required

# 前台页面的本bp
bp = Blueprint("home",__name__,url_prefix='/home')

# 前台主页
@bp.route('/',endpoint='index')
def index():
    content = {
        "user_id":None
    }
    return render_template('front/front_index.html', content=content)

# 前台用户注册，类视图
class SignUp(views.MethodView):
    def get(self,message=None):
        return render_template('front/front_signup.html',message=message)
    def post(self):
        # 得到表单数据
        form = LogUpForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password1.data
            username = form.petname.data
            phonenumble = form.phonenumble.data
            remember = form.remember.data
            # 数据库查找对应的邮箱信息
            emails = FrontUser.query.filter_by(email=email).first()
            if emails:
                # 得到错误信息并返回
                message = "已存在此邮箱"
                return self.get(message=message)
            # 数据库查找对应的名称信息
            usernames = FrontUser.query.filter_by(username=username).first()
            if usernames:
                # 得到错误信息并返回
                message = "已存在此名称"
                return self.get(message=message)
            # 数据库查找对应的邮箱信息
            phonenumbles = FrontUser.query.filter_by(phone_numble=phonenumble).first()
            if phonenumbles:
                # 得到错误信息并返回
                message = "已存在此手机号码"
                return self.get(message=message)
            user = FrontUser(username=username, password=password, email=email,phone_numble=phonenumble)
            db.session.add(user)
            db.session.commit()
            if remember:
                # 如果session.permanent = True
                # session的持久化日期为 31天
                session.permanent = True
            user = FrontUser.query.filter_by(email=email).first()
            session[config.Front_USER_ID] = user.id
            user_id = session.get(config.Front_USER_ID)
            front_user = FrontUser.query.get(user_id)
            g.front_user = front_user
            return redirect(url_for("home.login"))
        else:
            # 得到错误信息并返回
            message = form.get_errors()
            return self.get(message=message)
bp.add_url_rule('/signup/', view_func=SignUp.as_view('signup'))

# 前台用户登录，类视图
class FrontLogin(views.MethodView):
    def get(self,message=None):
        return render_template('front/front_login.html',message=message)
    def post(self):
        # 得到表单数据
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            # 数据库查找对应的用户信息
            user = FrontUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.Front_USER_ID] = user.id
                if remember:
                    # 如果session.permanent = True
                    # session的持久化日期为 31天
                    session.permanent = True
                return redirect(url_for('home.index'))
            else:
                return self.get(message="用户名或者密码错误")
        else:
            # 得到错误信息并返回
            message = form.get_errors()
            return self.get(message=message)
bp.add_url_rule('/login/',view_func=FrontLogin.as_view('login'))

# 前台用户注销
@bp.route('/logout/',endpoint='logout')
def logout():
    del session[config.Front_USER_ID]
    return redirect(url_for('home.login'))

# 前台个人中心
@bp.route('/profile/',endpoint='profile')
@login_required
def profile():
    return render_template('front/front_profile.html')

