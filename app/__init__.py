#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/9/30'
"""

import os
import tornado.web
from url import urls as urls
from settings import config


config_dict = config.get(os.environ.get('CONFIG_NAME', 'default'))

app = tornado.web.Application(
    handlers=urls,
    **config_dict
)

