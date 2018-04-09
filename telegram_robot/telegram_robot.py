#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 上午9:53
# @Author  : zhujinghui 
# @site    : 
# @File    : telegram_robot.py
# @Software: PyCharm

from telegram.ext import Updater
from telegram.ext import CommandHandler

import robot_web.app.db as db


updater = Updater(token='575865674:AAGR_AUZnNXsxVnSy1h6kUxwzDAe7sgAT6A',request_kwargs={'proxy_url':'socks5://127.0.0.1:1088'})
dispatcher = updater.dispatcher


#命令 。。。。。/caps
def bind(bot, update,args):
    print(args)
    print(update.message.from_user)
    print(update.message.from_user.id)
    print(update.message.from_user.first_name)
    print(update.message.from_user.last_name)
    # print(update.message['from']['id'])
    # print(update.message['from']['first_name'])
    if args == []:
        response_text = '请输入命令和邀请码！'
    else:

        response_text = '绑定成功！'
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)



bind_handler = CommandHandler('bind', bind, pass_args=True)


dispatcher.add_handler(bind_handler)


updater.start_polling()