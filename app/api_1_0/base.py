#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/9/30'
"""

import tornado.web
from torndsession.sessionhandler import SessionBaseHandler


class BaseHandler(SessionBaseHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")