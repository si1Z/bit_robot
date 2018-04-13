#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:17
# @Author  : zhujinghui 
# @site    : 
# @File    : run.py
# @Software: PyCharm

from app import app

if __name__ == '__main__':
    app.debug = False  # 设置调试模式，生产模式的时候要关掉debug
    app.run(
        host="0.0.0.0",
        port=8081
    )  # 启动服务器