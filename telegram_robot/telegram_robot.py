#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 上午9:53
# @Author  : zhujinghui 
# @site    : 
# @File    : telegram_robot.py
# @Software: PyCharm

from telegram.ext import Updater
from telegram.ext import CommandHandler

from config import token
from controller import controller_query,controller_bind


updater = Updater(token=token,request_kwargs={'proxy_url':'socks5://127.0.0.1:1088'})
dispatcher = updater.dispatcher

#命令 /bind   绑定
def bind(bot, update,args):
    code = args[0]
    user_id = update.message.from_user.id
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name


    if args == []:
        response_text = '请输入命令和邀请码！'
    else:
        controller_bind(code,user_id,first_name,last_name)
        response_text = '绑定成功！'
    bot.send_message(chat_id=update.message.chat_id, text=response_text)

bind_handler = CommandHandler('bind', bind, pass_args=True)
dispatcher.add_handler(bind_handler)


#命令 /query   查询
def query(bot, update,args):
    code = args[0]
    user_id = update.message.from_user.id
    if args == []:
        response_text = '请输入命令和邀请码！'
    else:

        response_text = controller_query(code,user_id)

    update.message.reply_text(response_text)

query_handler = CommandHandler('query', query, pass_args=True)
dispatcher.add_handler(query_handler)


updater.start_polling()
updater.idle()
