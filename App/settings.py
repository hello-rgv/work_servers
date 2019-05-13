'''
@Author: Mr Bean
@Date: 2019-05-12 00:24:52
@LastEditors: Mr Bean
@LastEditTime: 2019-05-12 00:26:06
@Description: file content
'''
import os


class BaseConfig():
    """基本配置"""

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')  # 模板文件的路径
    STATICFILES_DIR = os.path.join(BASE_DIR, 'static')  # 静态文件的路径
    JSON_AS_ASCII = False  # 处理 jsonify 中文乱码的方案

    # ========= Flask-SQLAlchemy 配置 ==================
    # 连接数据库字符串
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        BASE_DIR, 'data.sqlite')
    # 每次请求结束后是否自动提交数据库中的变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。
    # 这需要额外的内存， 如果不必要的可以禁用它。
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # ==================================================


class DevelopmentConfig(BaseConfig):
    """ 开发模式配置 """

    DEBUG = True


config = {'development': DevelopmentConfig}
