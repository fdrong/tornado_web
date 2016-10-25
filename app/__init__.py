#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/9/30'
"""

import os
import tornado.web
from .settings import urls
from .settings import Config
from .models import Base as DbBase
from .settings import get_session


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, handlers=urls, **Config)
        self.db = get_session(DbBase)



