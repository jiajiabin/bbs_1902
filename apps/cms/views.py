from flask import(
    Blueprint,
    render_template,
    views,
    request,
    session,
    redirect,
    url_for,
    g,
    jsonify
)
import config
from .forms import LoginForm,ChangeForm,ChangeEmailForm,PullBook
from .models import CMSUser
from .decorators import login_required
from exts import db
import qiniu
from ..books.models import Books,Author,Tags
from .url import ImgUrl

# 后台的蓝本bp
bp = Blueprint("cms",__name__,url_prefix='/cms')

# 后台首页
@bp.route('/',endpoint='index')
@login_required
def index():
    return render_template('cms/cms_index.html')

# 后台用户注销
@bp.route('/logout/',endpoint='logout')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))

# 后台个人中心
@bp.route('/profile/',endpoint='profile')
@login_required
def profile():
    return render_template('cms/cms_profile.html')

# 后台用户登录，类视图
class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template('cms/cms_login.html',message=message)
    def post(self):
        # 得到表单数据
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            # 数据库查找对应的用户信息
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    # 如果session.permanent = True
                    # session的持久化日期为 31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message="用户名或者密码错误")
        else:
            # 得到错误信息并返回
            message = form.get_errors()
            return self.get(message=message)
bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))

# 后台用户更改密码，类视图
class ChangePassword(views.MethodView):
    def get(self,message=None):
        message1 = None
        return render_template('cms/cms_chpassword.html',message=message,message1=message1)
    def post(self):
        # 得到表单数据
        form = ChangeForm(request.form)
        if form.validate():
            password1 = form.password1.data
            password2 = form.password2.data
            # 数据库查找对应的用户信息
            user = CMSUser.query.filter_by(email=g.cms_user.email).first()
            if user.check_password(password1):
                session[config.CMS_USER_ID] = user.id
                # 修改数据库数据
                user.password = password2
                db.session.commit()
                print("修改成功")
                message1="密码修改成功"
                return render_template('cms/cms_chpassword.html',message=None,message1=message1)
            else:
                return self.get(message="原始密码错误")
        else:
            # 得到错误信息并返回
            message = form.get_errors()
            return self.get(message=message)
bp.add_url_rule('/changepassword/',view_func=ChangePassword.as_view('changepassword'))

# 后台用户更改邮箱，类视图
class ChangeEmail(views.MethodView):
    def get(self,message=None):
        message1 = None
        return render_template('cms/cms_chemail.html',message=message,message1=message1)
    def post(self):
        # 得到表单数据
        form = ChangeEmailForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            email1 = form.email1.data
            # 数据库查找对应的用户信息
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                # 修改数据库数据
                user.email = email1
                db.session.commit()
                print("修改成功")
                message1="邮箱修改成功"
                return render_template('cms/cms_chemail.html',message=None,message1=message1)
            else:
                return self.get(message="邮箱或者密码错误")
        else:
            # 得到错误信息并返回
            message = form.get_errors()
            return self.get(message=message)
bp.add_url_rule('/changeemail/',view_func=ChangeEmail.as_view('changeemail'))

# 七牛上传绑定
@bp.route('/uptoken/')
def uptoken():
    access_key = config.ACCESS_KEY
    secret_key = config.SECRET_KEY
    q = qiniu.Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = config.BUCKET_NAME
    # 服务端生成 token
    # token = q.upload_token(bucket_name, key, 3600)
    token = q.upload_token(bucket_name)
    return jsonify({"uptoken":token})

# 后台上传图片
@bp.route("/upimg/", methods=['GET', 'POST'])
def upimg():
    if request.method == 'GET':
        return render_template('cms/pullimg.html')
    else:
        # 和前端约定好，发送网络请求，不管用户名和密码是   否验证成功
        # 我都返回同样格式的json对象给你
        # {"code":200,"message":""}
        imgInputval = request.form.get('imgInputval')
        return render_template('cms/pullimg.html')

# 后台上传书籍
@bp.route("/pullbook/", methods=['GET', 'POST'])
def pullbook():
    message1 = ""
    global ImgUrl
    if request.method == 'GET':
        return render_template('cms/pullbook.html', message1=message1)
    else:
        # 和前端约定好，发送网络请求，不管用户名和密码是   否验证成功
        # 我都返回同样格式的json对象给你
        # {"code":200,"message":""}
        if request.form.get('imgInputval'):
            ImgUrl = request.form.get('imgInputval')
        # 得到表单数据
        form = PullBook(request.form)
        if form.validate():
            name = form.name.data
            authors = form.author.data
            score = form.score.data
            # 数据库查找对应的用户信息
            books = Books.query.filter_by(bookname=name).first()
            if not books:
                # 修改数据库数据
                book1 = Books(bookname=name,score=score,bookimg=ImgUrl)
                authorlist = authors.split(",")
                for i in authorlist:
                    if i :
                        author1 = Author.query.filter_by(authorname=i).first()
                        if not author1:
                            author1 = Author(authorname=i)
                        author1.bookes.append(book1)
                        db.session.add(author1)
                db.session.commit()
                print("修改成功")
                message1 = "书籍添加成功，请点击添加书籍详细内容"
                return render_template('cms/pullbook.html',message1=message1)
            else:
                message1 = "以存在此书籍"
                return render_template('cms/pullbook.html',message1=message1)
        else:
            # 得到错误信息并返回
            message = form.get_errors()
            return render_template('cms/pullbook.html',message=message,message1=message1)


# 后台上传书籍内容
class PullBookText(views.MethodView):
    def get(self):

        return render_template('cms/pullbooktext.html')
    # def post(self):
    #     # 得到表单数据
    #     form = ChangeForm(request.form)
    #     if form.validate():
    #         password1 = form.password1.data
    #         password2 = form.password2.data
    #         # 数据库查找对应的用户信息
    #         user = CMSUser.query.filter_by(email=g.cms_user.email).first()
    #         if user.check_password(password1):
    #             session[config.CMS_USER_ID] = user.id
    #             # 修改数据库数据
    #             user.password = password2
    #             db.session.commit()
    #             print("修改成功")
    #             message1="密码修改成功"
    #             return render_template('cms/cms_chpassword.html',message=None,message1=message1)
    #         else:
    #             return self.get(message="原始密码错误")
    #     else:
    #         # 得到错误信息并返回
    #         message = form.get_errors()
    #         return self.get(message=message)
bp.add_url_rule('/pullbooktext/',view_func=PullBookText.as_view('pullbooktext'))