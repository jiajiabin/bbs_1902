from ..forms import BaseForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, Length, EqualTo


# {'password': ['密码长度在6-20位'], 'password_repeat': ['密码长度在6-20位', '两次密码必须一致']}

# 后台登录表单类
class LoginForm(BaseForm):
    email = StringField(validators=[Email(message="请输入正确的邮箱类型"), InputRequired(message="请输入邮箱")])
    password = StringField(validators=[Length(6, 20, message="请输入正确格式的密码")])
    remember = IntegerField()


# 后台修改密码表单类
class ChangeForm(BaseForm):
    password1 = StringField(validators=[Length(6, 20, message="请输入正确格式的密码")])
    password2 = StringField(validators=[Length(6, 20, message="请输入正确格式的密码")])
    password3 = StringField(validators=[Length(6, 20, message="请输入正确格式的密码"), EqualTo("password2", message="两次密码必须一致")])

# 后台修改邮箱表单类
class ChangeEmailForm(BaseForm):
    email = StringField(validators=[Email(message="请输入正确的邮箱类型"), InputRequired(message="请输入邮箱")])
    password = StringField(validators=[Length(6, 20, message="请输入正确格式的密码")])
    email1 = StringField(validators=[Email(message="请输入正确的邮箱类型"), InputRequired(message="请输入邮箱")])