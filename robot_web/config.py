#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:17
# @Author  : zhujinghui 
# @site    : 
# @File    : config.py
# @Software: PyCharm

import os
DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = ''
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'telegram_robot'

# 配置和数据库的连接信息
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/telegram_robot?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False