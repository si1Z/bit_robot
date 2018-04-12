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



#定义基类
Base=declarative_base()


class Wallet(Base):
    __tablename__ = 'wallet'

    #     #修改数据表配置
    #     __table_args__={
    #         'mysql_engine':'InnoDB',
    #         'mysql_charset':'utf8'
    #     }

    wallet = Column(String(512), primary_key=True, unique=True)
    code = Column(String(256), index=True, unique=True)
    user_id = Column(Integer)
    first_name = Column(String(256))
    last_name = Column(String(256))
    num = Column(Integer)

    def __repr__(self):
        return '<Wallet %r>' % "wallet"

if __name__ == '__main__':
    #初始化数据库连接对象
    engine=create_engine(CONSTR,echo=True)
    db_session=sessionmaker(bind=engine)
    session=db_session()
    query = session.query(Wallet)

    # wallet=Wallet(wallet='kikay',code=20)
    #添加


    # session.add(wallet)
    # #提交
    # session.commit()
    # #关闭
    # session.close()



    # print(query1.first().wallet)



    # query.filter(Wallet.wallet=='kikay').update({Wallet.code:'Tom2'})
    # session.commit()


    # result = query.filter(Wallet.user_id == 555934414)
    # print(result[0].count)