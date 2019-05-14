#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Mr Bean
@Date: 2019-05-12 14:31:57
@LastEditors: Mr Bean
@LastEditTime: 2019-05-14 09:38:25
@Description: file content
'''
from . import Classify
from .models import Classify as mClassify
from logzero import logger
from flask import request, jsonify, json
from App import db
from sqlalchemy import or_
from App.MyToos import KTools


@Classify.route('/')
def index():
    return 'api baseinfo Classify index.'


@Classify.route('/add', methods=['POST', 'GET'])
def add():
    rsp_json = None
    if request.method == 'POST':
        logger.info('Classify.add 接收到一个POST请求!')
        rqs_data = json.loads(request.data)
        rsp_json = db_add(rqs_data)
    elif request.method == 'GET':
        logger.info('Classify.add 接收到一个GET请求!')
        rsp_json = {"status": "error", "msg": "还没有设计GET请求!"}

    return jsonify(rsp_json)


@Classify.route('/delete', methods=['POST', 'GET'])
def delete():
    rsp_json = None
    if request.method == 'POST':
        logger.info('Classify.delete 接收到一个POST请求!')
        rqs_data = json.loads(request.data)
        rsp_json = db_delete(rqs_data)
    elif request.method == 'GET':
        logger.info('Classify.delete 接收到一个GET请求!')
        rsp_json = {"status": "error", "msg": "还没有设计GET请求!"}

    return jsonify(rsp_json)
    return 'del'


@Classify.route('/update', methods=['POST', 'GET'])
def update():
    rsp_json = None
    if request.method == 'POST':
        logger.info('Classify.update 接收到一个POST请求!')
        rqs_data = json.loads(request.data)
        rsp_json = db_update(rqs_data)
    return jsonify(rsp_json)


@Classify.route('/search', methods=['POST', 'GET'])
def search():
    rsp_json = None
    if request.method == 'POST':
        logger.info('Classify.search 接收到一个POST请求!')
        rqs_data = json.loads(request.data)
        rsp_json = db_search(rqs_data)
    elif request.method == 'GET':
        logger.info('Classify.search 接收到一个GET请求!')
        rsp_json = {"status": "error", "msg": "还没有设计GET请求!"}

    return jsonify(rsp_json)


def db_add(rqs_data):
    try:
        name = rqs_data['name']
        mclassify = mClassify(name)
        db.session.add(mclassify)
        db.session.commit()
        return {"status": "success"}
    except Exception as e:
        error_msg = "向数据库添加数据时,发生异常!"
        logger.error(error_msg)
        print(e)
        return {"status": "error", "msg": error_msg}


def db_search(rqs_data):
    search_value = rqs_data['value']
    if search_value != '':
        try:
            mclassify = mClassify.query.filter(
                or_(mClassify.id.like("%" + search_value + "%"),
                    mClassify.name.like("%" + search_value + "%"),
                    mClassify.pinyin.like("%" + search_value + "%"))).all()
            return {"status": "success", "rsp_data": KTools.dbToDict(mclassify)}
        except Exception as e:
            error_msg = "向数据库添加数据时,发生异常!"
            logger.error(error_msg)
            print(e)
            return {"status": "error", "msg": error_msg}

def db_update(rqs_data):

    try:
        mclassify = mClassify.query.filter_by(id=rqs_data['update_data']['id']).first()
        mclassify.name = rqs_data['update_data']['name']
        mclassify.pinyin = KTools.cnToPinYin(rqs_data['update_data']['name'])
        db.session.add(mclassify)
        db.session.commit()
        return {'status': 'success'}
    except Exception as e:
        error_msg = '向数据库更新数据时,发生异常!'
        logger.error(e)
        return {'status': 'error', 'msg': error_msg}

def db_delete(rqs_data):
    try:
        mclassify = mClassify.query.filter_by(id=rqs_data['id']).first()
        db.session.delete(mclassify)
        db.session.commit()
        return {'status': 'success'}
    except Exception as e:
        error_msg = '向数据库删除数据时,发生异常!'
        logger.error(e)
        return {'status': 'error', 'msg': error_msg}