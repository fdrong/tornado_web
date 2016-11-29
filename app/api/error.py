#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/11/29'
"""

import tornado.web


class PageNotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        raise tornado.web.HTTPError(404)