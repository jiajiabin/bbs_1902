from wtforms import Form

# 返回错误信息的表单类
class BaseForm(Form):
    def get_errors(self):
        message = self.errors.popitem()[1][0]
        return message