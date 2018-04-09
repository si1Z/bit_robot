#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:14
# @Author  : zhujinghui 
# @site    : 
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask  # 引入 flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)  # 实例化一个flask 对象

app.config.from_object('config')  # 载入配置文件

db = SQLAlchemy(app)  # 初始化 db 对象


from . import views, models # 导入 views 模块