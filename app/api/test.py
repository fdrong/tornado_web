#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/17'
"""

from app.api import BaseHandler
import tornado.web
import tornado.gen
from app.tasks import add
import time


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


class CeleryTaskHandler(BaseHandler):
    def get(self):
        self.logger.info("calling get ")
        x = 10
        y = 2
        add.delay(x, y)
        self.write("test for celery task")


class GenTaskHandler(BaseHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        yield tornado.gen.Task(self.test, "abc")
        self.write("test for coroutine sleep")

    def test(self, x, callback=None):
        print "test %s" % x
        time.sleep(5)
        print "sleep over"
        callback(x)

