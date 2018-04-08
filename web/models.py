#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午2:29
# @Author  : zhujinghui 
# @site    : 
# @File    : models.py
# @Software: PyCharm

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    fabu_id = db.Column(db.Integer, db.ForeignKey('fabu.id'))
    creat_time = db.Column(db.DateTime, default=datetime.now)
    detail = db.Column(db.Text, nullable=False)
    fabu = db.relationship('Fabu',
                           backref=db.backref('comments', order_by=creat_time.desc))  # order_by=creat_time.desc按时间降序
    author = db.relationship('User', backref=db.backref('comments'))