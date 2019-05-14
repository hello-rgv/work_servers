#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Mr Bean
@Date: 2019-05-12 14:32:18
@LastEditors: Mr Bean
@LastEditTime: 2019-05-14 09:36:07
@Description: file content
'''
from App import db
from App.MyToos import KTools


class Classify(db.Model):
    '''商品单位数据库模型'''
    __tablename__ = 'Classify'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    pinyin = db.Column(db.String(50), index=True)

    def __init__(self, name):
        self.name = name
        self.pinyin = KTools.cnToPinYin(name)

    def __repr__(self):
        return '<Classify %r>' % self.name
