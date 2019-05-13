#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Mr Bean
@Date: 2019-05-12 14:31:57
@LastEditors: Mr Bean
@LastEditTime: 2019-05-12 17:23:12
@Description: file content
'''
from . import Unit
from .models import Unit as mUnit
from logzero import logger
from flask import request, jsonify, json
from App import db
from sqlalchemy import or_


@Unit.route('/')
def index():
    return 'api baseinfo unit index.'


@Unit.route('/add', methods=['POST', 'GET'])
def add():
    rsp_json = None
    if request.method == 'POST':
        logger.info('Unit.add 接收到一个POST请求!')
        rqs_data = json.loads(request.data)
        rsp_json = db_add(rqs_data)
    elif request.method == 'GET':
        logger.info('Unit.add 接收到一个GET请求!')
        rsp_json = {"status": "error", "msg": "还没有设计GET请求!"}

    return jsonify(rsp_json)


@Unit.route('/del', methods=['POST', 'GET'])
def remove():
    return 'del'


@Unit.route('/update', methods=['POST', 'GET'])
def db_update():
    return 'update'


@Unit.route('/search', methods=['POST', 'GET'])
def search():
    rsp_json = None
    if request.method == 'POST':
        logger.info('Unit.search 接收到一个POST请求!')
        rqs_data = json.loads(request.data)
        rsp_json = db_search(rqs_data)
    elif request.method == 'GET':
        logger.info('Unit.search 接收到一个GET请求!')
        rsp_json = {"status": "error", "msg": "还没有设计GET请求!"}

    return jsonify(rsp_json)


def db_add(rqs_data):
    try:
        name = rqs_data['name']
        munit = mUnit(name)
        db.session.add(munit)
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
            munit = mUnit.query.filter(
                or_(mUnit.id.like("%" + search_value + "%"),
                    mUnit.name.like("%" + search_value + "%"),
                    mUnit.pinyin.like("%" + search_value + "%"))).all()
            return {"status": "success", "rsp_data": toDict(munit)}
        except Exception as e:
            error_msg = "向数据库添加数据时,发生异常!"
            logger.error(error_msg)
            print(e)
            return {"status": "error", "msg": error_msg}


def toDict(val):
    """
    把查询返回的数据处理成列表

    Parameters:
        val - 查询返回的数据

    Returns:
        返回列表(list)

    """
    result_json = []
    for item in val:
        tmp_dict = {"id": item.id, "name": item.name}
        result_json.append(tmp_dict)
    return result_json
    