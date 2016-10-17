#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/9/30'
"""

import os

# 开发环境
DevelopmentConfig = {
    "debug": True,
    "allow_remote_access": True,
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), 'static'),
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    "xsrf_cookies": True,
    "login_url": "/login",
    # redis session config
    "driver": "redis",
    "driver_settings":{
        "host": 'localhost',
        "port": 6379,
        "db": 0,
        "max_connections": 1024,
    }

}

# 测试环境
TestingConfig = {
    "debug": True,
    "allow_remote_access": True,
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), 'static'),
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    "xsrf_cookies": True,
    "login_url": "/login",
    # redis session config
    "driver": "redis",
    "driver_settings":{
        "host": 'localhost',
        "port": 6379,
        "db": 0,
        "max_connections": 1024,
    }
}


# 生产环境
ProductionConfig = {
    "debug": True,
    "allow_remote_access": True,
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), 'static'),
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    "xsrf_cookies": True,
    "login_url": "/login",
    # redis session config
    "driver": "redis",
    "driver_settings":{
        "host": 'localhost',
        "port": 6379,
        "db": 0,
        "max_connections": 1024,
    }
}

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}