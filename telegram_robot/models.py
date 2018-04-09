#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 下午5:28
# @Author  : zhujinghui 
# @site    : 
# @File    : models.py
# @Software: PyCharm
#导入相关库
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy import text,or_,not_,update
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy import ForeignKey

#MySQL数据库连接字符串
CONSTR='mysql+pymysql://root:@localhost/telegram_robot?charset=utf8'

#定义基类
Base=declarative_base()

# class Wallet(Base):
#     #显示声明关联的数据表名称
#     __tablename__='wallet'
#
#     #修改数据表配置
#     __table_args__={
#         'mysql_engine':'InnoDB',
#         'mysql_charset':'utf8'
#     }
#     #主键Id
#     #钱包地址：非空
#     wallet=Column(String(512),nullable=False)
#     #邀请码:非空
#     code=Column(String(256),nullable=False)
#     #外键对象
#     #jobs=relationship('job')

class Wallet(Base):
    __tablename__ = 'wallet'
    wallet = Column(String(512), primary_key=True, unique=True)
    code = Column(String(256), index=True, unique=True)

    def __repr__(self):
        return '<Wallet %r>' % "wallet"


#初始化数据库连接对象
engine=create_engine(CONSTR,echo=True)
db_session=sessionmaker(bind=engine)
session=db_session()

# wallet=Wallet(wallet='kikay',code=20)
# #添加
# session.add(wallet)
# #提交
# session.commit()
# #关闭
# session.close()


query1=session.query(Wallet)
print(query1.first().wallet)