from ..forms import BaseForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, Length, EqualTo,Regexp


# 前台注册表单类
class LogUpForm(BaseForm):
    email = StringField(validators=[Email(message="请输入正确的邮箱类型"), InputRequired(message="请输入邮箱")])
    password1 = StringField(validators=[Length(6, 20, message="请输入正确格式的密码")])
    password2 = StringField(validators=[Length(6, 20, message="请输入正确格式的密码"), EqualTo("password1", message="两次密码必须一致")])
    petname = StringField(validators=[Length(2, 20, message="长度不符合要求"), InputRequired(message="请输入昵称")])
    phonenumble = StringField(validators=[Regexp(r'1[3-9]\d{9}',message="请输入正确格式的手机号"),InputRequired(message="请输入邮箱")])
    remember = IntegerField()

# 前台登录表单类
class LoginForm(BaseForm):
    email = StringField(validators=[Email(message="请输入正确的邮箱类型"), InputRequired(message="请输入邮箱")])
    password = StringField(validators=[Length(6, 20, message="请输入正确格式的密码")])
    remember = IntegerField()