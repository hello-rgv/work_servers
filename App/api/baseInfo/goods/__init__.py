#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Mr Bean
@Date: 2019-05-12 00:32:05
@LastEditors: Mr Bean
@LastEditTime: 2019-05-12 09:38:46
@Description: 创建 商品信息 蓝图

'''


from flask import Blueprint

Goods = Blueprint('goods', __name__)

from . import views, models
