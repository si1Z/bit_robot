#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 上午9:36
# @Author  : zhujinghui 
# @site    : 
# @File    : main.py
# @Software: PyCharm

from flask import Flask
from flask import render_template, redirect,url_for
from flask import request
import hashlib

app = Flask(__name__)


def wallet2hash(wallet_address):
    hash = hashlib.md5()  # md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
    hash.update(bytes('{}'.format(wallet_address), encoding='utf-8'))  # 要对哪个字符串进行加密，就放这里
    return hash.hexdigest()  # 拿到加密字符串

telegram_invite_link = "https://t.me/joinchat/ISLizhCQ4djj5zoeqVgMGw"




@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='GET':
        return render_template('index.html')


    #记录下钱包地址
    wallet_address = request.form.get('wallet_address')
    #记录下钱包地址哈希值
    wallet_hash = wallet2hash(wallet_address)
    return '{}/{}'.format('http://127.0.0.1:5000',wallet_hash)


@app.route('/<a_code>', methods=['GET','POST'])
def invite(a_code):
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        # 记录下钱包地址
        wallet_address = request.form.get('wallet_address')
        print(wallet_address)
        # 记录下钱包地址哈希值
        b_code = wallet2hash(wallet_address)

        invite_url = '{}/{}'.format('http://127.0.0.1:5000',b_code)

        join_url = "http://127.0.0.1:5000/join/{a_code}/{b_code}".format(a_code=a_code,b_code=b_code)
        return render_template('result.html',invite_url=invite_url,join_url=join_url)

@app.route('/join/<a_code>/<b_code>', methods=['GET','POST'])
def join(a_code,b_code):
    print(a_code)
    print(b_code)

    return redirect(telegram_invite_link)


# @app.route('/login', methods=['POST','GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username']=='admin':
#             return redirect(url_for('home',username=request.form['username']))
#         else:
#             error = 'Invalid username/password'
#     return render_template('login.html', error=error)
#
# @app.route('/home')
# def home():
#     return render_template('home.html', username=request.args.get('username'))

if __name__ == '__main__':
    app.debug = True
    app.run()