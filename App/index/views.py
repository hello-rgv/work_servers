#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Mr Bean
@Date: 2019-05-12 09:56:02
@LastEditors: Mr Bean
@LastEditTime: 2019-05-12 15:40:20
@Description: 首页 视图
'''

from App import app, db


@app.route('/')
def index():
    return 'Welcome to Home'


@app.route('/db_create')
def db_create():
    db.drop_all()
    db.create_all()
    return 'db_create'
