#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Mr Bean
@Date: 2019-05-12 00:33:37
@LastEditors: Mr Bean
@LastEditTime: 2019-05-12 09:55:26
@Description: 商品信息 数据库模型
'''

from App import db


class Goods(db.Model):
    """商品信息库"""
    __tablename__ = "Goods"
    # 商品货号
    id = db.Column(db.String(10), primary_key=True, unique=True, nullable=False)
    # 商品名称
    name = db.Column(db.String(100), nullable=False)
    # 商品名称拼音首字母
    pinyin = db.Column(db.String(50), nullable=False, index=True)
    # 商品规格
    specs = db.Column(db.String(20), nullable=False)
    # 商品售价
    prices = db.Column(db.Float, nullable=False)
    # 商品类别
    classify = db.Column(db.String(20), nullable=False)
    # 销售单位
    unit = db.Column(db.String(4), nullable=False)

    def __repr__(self):
        # 非必须，用于调试、测试时返回一个具有可读性的字符串表示模型
        return '<Goods %r>' % self.name
