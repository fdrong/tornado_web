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
import os
import tornado.options
import logging
from app.api_1_0.base import LogFormatter
from app import app, config_dict


from tornado.options import define, options
define("host", default='127.0.0.1', help="run on the given port", type=str)
define("port", default=8000, help="run on the given port", type=int)

# 日志配置
define("login", default="debug")
define("log_file_prefix", default=os.path.join(config_dict['log_path'], "tornado_main.log"))
define("log_rotate_mode", default='time')   # 轮询模式: time or size
define("log_rotate_when", default='D')      # 单位: S / M / H / D / W0 - W6
define("log_rotate_interval", default=1)
define("log_to_stderr", default=True)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    [i.setFormatter(LogFormatter()) for i in logging.getLogger().handlers]
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

# if __name__ == '__main__':
#     tornado.options.parse_command_line()
#     wsgi_app = tornado.wsgi.WSGIAdapter(app)
#     server = wsgiref.simple_server.make_server(options.host, options.port, wsgi_app)
#     server.serve_forever()