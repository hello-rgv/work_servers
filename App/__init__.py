'''
@Author: Mr Bean
@Date: 2019-05-12 00:21:38
@LastEditors: Mr Bean
@LastEditTime: 2019-05-12 10:04:37
@Description: 创建 Flask
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .settings import config

app = Flask(__name__)
db = SQLAlchemy()

from .index import views


def create_app():
    '''
    创建 Flask
    '''
    app.config.from_object(config['development'])
    db.init_app(app)
    CORS(app=app)
    return app
