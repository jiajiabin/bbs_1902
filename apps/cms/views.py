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
from .forms import LoginForm,ChangeForm,ChangeEmailForm
from .models import CMSUser
from .decorators import login_required
from exts import db
from qiniu import Auth,put_data,etag

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

def upload_file_qiniu(inputdata):
    access_key = config.ACCESS_KEY
    secret_key = config.SECRET_KEY
    # :param inputdata: bytes类型的数据
    # :return: 文件在七牛的上传名字
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    #要上传的空间
    bucket_name = config.BUCKET_NAME
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name)
    #如果需要对上传的图片命名，就把第二个参数改为需要的名字
    ret1,ret2=put_data(token,None,data=inputdata)
    #判断是否上传成功
    if ret2.status_code!=200:
        raise Exception('文件上传失败')
    return ret1.get('key')

@bp.route('/uptoken',methods=['post','GET'])
def uptoken():
    session1 = None
    src = None
    if request.method == 'GET':
        return render_template('cms/pullimg.html')
    if request.method == 'POST':
        # 获取前端数据
        try:
            data = request.files.get('imgup').read()
        except Exception as e:
            return jsonify(errmsg='获取前端数据错误')
        # 使用自定义的上传文件系统，上传图片服务器
        try:
            filename = upload_file_qiniu(data)
            src = "http://py645ayfc.bkt.clouddn.com/" + filename
            session1 = "上传成功"
        except Exception as e:
            return  jsonify(errmsg='上传失败')
    return render_template('cms/pullimg.html',session1=session1,src=src)