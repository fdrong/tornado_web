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
from tornado import httpclient
from app.tasks import add
import time
import json


class RedisSessionHandler(BaseHandler):

    def get(self):
        # yield self.divide(1, 1)
        self.write("Redis Session Example:<br/>")
        if 'sv' in self.session:
            sv = self.session["sv"]
        else:
            sv = 0
        time.sleep(100)
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
        a = yield tornado.gen.Task(self.test, "sleep 15s")
        print a.read()
        self.write("test for coroutine sleep")

    def test(self, x, callback=None):
        print "test %s" % x
        time.sleep(15)
        print "sleep over"
        callback(x)
        return "123"


class AsycTesthandler(BaseHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        self.logger.info("test")
        client = httpclient.AsyncHTTPClient()
        data = dict()
        data['title'] = 'fury'
        response = yield tornado.gen.Task(client.fetch, "http://www.oschina.net/", method='POST', body=json.dumps(data))
        self.on_response(response)

    def on_response(self, resp):
        self.write("hello world")
        # body = json.loads(resp.body)
        # if body == None:
        #     self.write("error")
        # else:
        #     self.write(body)
        return