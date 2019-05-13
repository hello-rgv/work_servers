#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Mr Bean
@Date: 2019-05-12 00:33:27
@LastEditors: Mr Bean
@LastEditTime: 2019-05-12 09:59:57
@Description: 商品信息 视图
'''

from . import Goods
from flask import request, jsonify
from logzero import logger


@Goods.route('/')
def index():
    return 'Welcome to api Goods.'


@Goods.route('/add', methods=['POST', 'GET'])
def add():
    '''
    添加数据
    '''
    result_json = None  # 返回给前端的json
    if request.method == 'POST':
        logger.info('api.baseInfo.goods 接收到了一个POST请求!')
        result_json = {'status': 'success'}
    else:
        logger.info('api.baseInfo.goods 接收到了一个GET请求!')
        result_json = {'status': 'error', 'msg': '还没有设计GET请求!'}

    return jsonify(result_json)
