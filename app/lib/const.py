#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/12/2'
"""

class Permission:
    UserList = 'user_list'
    UserAdd = 'user_add'
    UserEdit = 'user_edit'


class Regex:
    Phone = '^1(3[0-9]|4[57]|5[0-35-9]|7[0135678]|8[0-9])\d{8}$'
    Mail = '\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}'

# IP白名单
IpWhiteList = [
]