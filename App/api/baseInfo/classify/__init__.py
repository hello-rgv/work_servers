#!/usr/bin/env python
# coding=UTF-8
'''
@Author: Mr Bean
@Date: 2019-05-12 14:31:22
@LastEditors: Mr Bean
@LastEditTime: 2019-05-14 09:35:45
@Description: file content
'''
from flask import Blueprint

Classify = Blueprint('classify', __name__)

from . import views, models
