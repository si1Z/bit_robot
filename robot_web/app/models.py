#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/8 下午3:16
# @Author  : zhujinghui 
# @site    : 
# @File    : models.py
# @Software: PyCharm

from . import db

class Wallet(db.Model):
    __tablename__ = 'wallet'
    wallet = db.Column(db.String(512), primary_key=True, unique=True)
    code = db.Column(db.String(256), index=True, unique=True)

    def __repr__(self):
        return '<Wallet %r>' % "wallet"


class Relation(db.Model):
    __tablename__ = 'relation'
    id = db.Column(db.INT, primary_key=True, unique=True)
    a_code = db.Column(db.String(256), index=True, unique=True)
    b_code = db.Column(db.String(256), index=True, unique=True)

    def __repr__(self):
        return '<Relation %r>' % "relation"