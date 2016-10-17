#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/17'
"""

from base import BaseHandler


class RedisSessionHandler(BaseHandler):

    def get(self):
        # yield self.divide(1, 1)
        self.write("Redis Session Example:<br/>")
        if 'sv' in self.session:
            sv = self.session["sv"]
        else:
            sv = 0
        self.write('Current Session Value:%s' % sv)
        self.session['sv'] = sv + 1

    def divide(self, x, y):
        print x/y