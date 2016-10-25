#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/9/30'
"""
import os
import tornado.web
import logging
import tornado.log
from datetime import date
from logging.handlers import TimedRotatingFileHandler
from torndsession.sessionhandler import SessionBaseHandler


class BaseHandler(SessionBaseHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

    @property
    def logger(self):
        return tornado.log.app_log

    @property
    def db(self):
        return self.application.db


class LogFormatter(tornado.log.LogFormatter):
    def __init__(self):
        super(LogFormatter, self).__init__(
            # fmt="%(color)s[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s]%(end_color)s %(message)s",
            fmt="%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )