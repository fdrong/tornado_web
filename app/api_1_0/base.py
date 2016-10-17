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
from settings import config


class BaseHandler(SessionBaseHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

    @property
    def logger(self):
        tornado.log.LogFormatter(fmt='%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s', datefmt="%Y-%m-%d %H:%M:%S")
        return tornado.log.app_log
        # """
        # 创建一个日志对象logger，同时打印文件日志和终端日志，其中Debug级别的日志只在终端打印
        # """
        # config_dict = config.get(os.environ.get('CONFIG_NAME', 'default'))
        # LOG_FILE = os.path.join(config_dict["log_path"], "{}.log".format(date.today()))
        # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s',
        #                               datefmt='%Y-%m-%d %H:%M:%S')  # 格式化日志
        # file_handler = TimedRotatingFileHandler(LOG_FILE,'D', 1, 0)  # 实例化handler
        # file_handler.suffix = "%Y-%m-%d.log"
        # file_handler.setFormatter(formatter)
        # file_handler.setLevel(logging.INFO)  # 设置文件日志打印级别
        #
        # console_handler = logging.StreamHandler()  # 设置终端日志打印
        # console_handler.setLevel(logging.DEBUG)  # 设置终端日志打印级别
        # console_handler.setFormatter(formatter)  # 设置终端日志打印格式
        #
        # logger = logging.getLogger("")  # 获取名为log_name的logger
        # # logger = get_task_logger(name)
        # logger.addHandler(file_handler)  # 添加Handler
        # logger.addHandler(console_handler)  # 添加Handler
        # logger.setLevel(logging.INFO)  # 设置日志级别为DEBUG(级别最低)
        # return logger