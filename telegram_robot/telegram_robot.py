#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 上午9:53
# @Author  : zhujinghui 
# @site    : 
# @File    : telegram_robot.py
# @Software: PyCharm

from telegram.ext import Updater
from telegram.ext import CommandHandler

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Wallet
from config import token,CONSTR


#初始化数据库连接对象
engine=create_engine(CONSTR,echo=True)
db_session=sessionmaker(bind=engine)
session=db_session()
query = session.query(Wallet)

updater = Updater(token=token,request_kwargs={'proxy_url':'socks5://127.0.0.1:1088'})
dispatcher = updater.dispatcher




#命令 /bind   绑定
def bind(bot, update,args):

    code = args[0]


    # print(args)
    # print(update.message.from_user)
    # print(update.message.from_user.id)
    # print(update.message.from_user.first_name)
    # print(update.message.from_user.last_name)
    # print(update.message['from']['id'])
    # print(update.message['from']['first_name'])
    if args == []:
        response_text = '请输入命令和邀请码！'
    else:
        query.filter(Wallet.code == code).update(
            {Wallet.user_id: update.message.from_user.id, Wallet.first_name: update.message.from_user.first_name,
             Wallet.last_name: update.message.from_user.last_name})
        session.commit()
        response_text = '绑定成功！'
    bot.send_message(chat_id=update.message.chat_id, text=response_text)
bind_handler = CommandHandler('bind', bind, pass_args=True)
dispatcher.add_handler(bind_handler)


#命令 /query   查询
def query(bot, update,args):

    code = args[0]

    # print(args)
    # print(update.message.from_user)
    # print(update.message.from_user.id)
    # print(update.message.from_user.first_name)
    # print(update.message.from_user.last_name)
    # print(update.message['from']['id'])
    # print(update.message['from']['first_name'])
    if args == []:
        response_text = '请输入命令和邀请码！'
    else:
        print(code)
        result = query.filter(Wallet.code == code)
        response_text = result[0].count

    bot.send_message(chat_id=update.message.chat_id, text=response_text)

query_handler = CommandHandler('query', query, pass_args=True)
dispatcher.add_handler(query_handler)


# #命令 /query   查询
# def query(bot, update,args):
#
#     code = args[0]
#
#
#     # print(args)
#     # print(update.message.from_user)
#     # print(update.message.from_user.id)
#     # print(update.message.from_user.first_name)
#     # print(update.message.from_user.last_name)
#     # print(update.message['from']['id'])
#     # print(update.message['from']['first_name'])
#     if args == []:
#         response_text = '请输入命令和邀请码！'
#     else:
#         print(code)
#         query.filter(Wallet.code == code).update(
#             {Wallet.user_id: update.message.from_user.id, Wallet.first_name: update.message.from_user.first_name,
#              Wallet.last_name: update.message.from_user.last_name})
#         session.commit()
#         response_text = '绑定成功！'
#     bot.send_message(chat_id=update.message.chat_id, text=response_text)
# bind_handler = CommandHandler('query', query, pass_args=True)
# dispatcher.add_handler(bind_handler)






# updater.start_polling()


result = query.filter(Wallet.code == '7c7f3edd5dc256c8d9beeb63f4d35812')
response_text = result[0].count
print(response_text)