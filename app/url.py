#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/9/30'
"""
from app.api_1_0.login import WelcomeHandler, LoginHandler, LogoutHandler
from app.api_1_0.test import RedisSessionHandler, CeleryTaskHandler

# 首页
urls = [
    (r'/', WelcomeHandler),
]

# 登录
urls += [
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),

]

# 测试
urls += [
    (r'/test/redis_session', RedisSessionHandler),
    (r'/test/celery_task', CeleryTaskHandler)
]