#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 下午2:43
# @Author  : zhujinghui 
# @site    : 
# @File    : te.py
# @Software: PyCharm

from telegram.ext import Updater
# pp = telegram.utils.request.Request(con_pool_size=1, proxy_url='socks5://127.0.0.1:1088', urllib3_proxy_kwargs=None, connect_timeout=5.0, read_timeout=5.0)


updater = Updater(token='575865674:AAGR_AUZnNXsxVnSy1h6kUxwzDAe7sgAT6A',request_kwargs={'proxy_url':'socks5://127.0.0.1:1088'})

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)



from telegram.ext import CommandHandler

#命令    /start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#命令 。。。。。/caps
def caps(bot, update, args):
    if args == []:
        text_caps = '没有输入数据'
    else:
        text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)


from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
    InlineQueryResultArticle(
        id=query.upper(),
        title='Caps',
        input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)




#命令    /query
def query(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)






import requests
from telegram.ext import MessageHandler, Filters

#。。。。。。。。。文本
def echo(bot, update):
    ask = update.message.text
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg={}".format(ask)
    answer_obj = requests.get(url).json()

    if answer_obj['result'] ==0:

        answer = answer_obj['content'].replace('{br}','\n')
    else:
        answer = '没听懂！'
    bot.send_message(chat_id=update.message.chat_id, text=answer)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

#..............图片
def photo(bot, update):
    ask = update.message.photo
    print(ask)
    bot.send_message(chat_id=update.message.chat_id, text="保存")

photo_handler = MessageHandler(Filters.photo, photo)
dispatcher.add_handler(photo_handler)

#...............文件
def file(bot, update):
    ask = update.message.document
    print(ask)
    with open(ask['file_name'],'wb') as f:
        ask.download(out=f)

    bot.send_message(chat_id=update.message.chat_id, text="保存")

file_handler = MessageHandler(Filters.document, file)
dispatcher.add_handler(file_handler)





from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()