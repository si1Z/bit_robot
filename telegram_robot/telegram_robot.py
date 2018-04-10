#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 上午9:53
# @Author  : zhujinghui 
# @site    : 
# @File    : telegram_robot.py
# @Software: PyCharm

from telegram.ext import Updater
from telegram.ext import CommandHandler
from models import Wallet,query,session
from config import token


updater = Updater(token=token,request_kwargs={'proxy_url':'socks5://127.0.0.1:1088'})
dispatcher = updater.dispatcher


#命令 。。。。。/caps
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
        print(code)
        query.filter(Wallet.code == code).update(
            {Wallet.user_id: update.message.from_user.id, Wallet.first_name: update.message.from_user.first_name,
             Wallet.last_name: update.message.from_user.last_name})
        session.commit()
        response_text = '绑定成功！'
    bot.send_message(chat_id=update.message.chat_id, text=response_text)



bind_handler = CommandHandler('bind', bind, pass_args=True)


dispatcher.add_handler(bind_handler)


updater.start_polling()


# query.filter(Wallet.code == '47bce5c74f589f4867dbd57e9ca9f808').update(
#             {Wallet.user_id: 12345, Wallet.first_name: 'abc',
#              Wallet.last_name: 'def'})
#
# session.commit()