#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/13 下午6:53
# @Author  : zhujinghui 
# @site    : 
# @File    : controller.py
# @Software: PyCharm

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Wallet
from config import token,CONSTR

#初始化数据库连接对象
engine=create_engine(CONSTR,echo=True)
db_session=sessionmaker(bind=engine)
session=db_session()
query1 = session.query(Wallet)

#命令 /bind   绑定
def controller_bind(code,user_id,first_name,last_name):

    query1.filter(Wallet.code == code).update(
        {Wallet.user_id: user_id, Wallet.first_name: first_name,
         Wallet.last_name:last_name})
    session.commit()
    response_text = '绑定成功！'
    return response_text


# 命令 /query   查询
def controller_query(code, user_id):

    result = query1.filter(Wallet.code == code, Wallet.user_id == user_id)
    response_text = result[0].num

    return response_text
