#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/9/30'
"""

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import wsgiref.simple_server
import tornado.options
from app import app


from tornado.options import define, options
define("host", default='127.0.0.1', help="run on the given port", type=str)
define("port", default=8000, help="run on the given port", type=int)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

# if __name__ == '__main__':
#     tornado.options.parse_command_line()
#     wsgi_app = tornado.wsgi.WSGIAdapter(app)
#     server = wsgiref.simple_server.make_server(options.host, options.port, wsgi_app)
#     server.serve_forever()