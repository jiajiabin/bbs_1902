from flask import Flask
import config
from exts import db
from apps.cms import bp as cms_bp
from apps.front import bp as front_bp
from apps.common import bp as common_bp
from apps.books import bp as book_bp
from apps.msg import bp as msg_bp
from ueditor import bp as ueditor_bp
# 表单提交防止跨站请求伪造
from flask_wtf import CSRFProtect


def create_app():
    app = Flask(__name__)
    # 绑定蓝本bp
    app.register_blueprint(cms_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(book_bp)
    app.register_blueprint(msg_bp)
    app.register_blueprint(ueditor_bp)
    # 导入配置文件并且生效
    app.config.from_object(config)
    # 初始化
    db.init_app(app)
    # 表单提交防止跨站请求伪造
    CSRFProtect(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,host="0.0.0.0",port=8888)
