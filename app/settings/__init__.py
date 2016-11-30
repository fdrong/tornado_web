#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/25'
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/9/30'
"""

import os

BaseDir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# 开发环境
DevelopmentConfig = {
    "debug": True,
    "allow_remote_access": True,
    "template_path": os.path.join(BaseDir, "templates"),
    "static_path": os.path.join(BaseDir, 'static'),
    "log_path" : os.path.join(BaseDir, 'logs'),
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",

    "xsrf_cookies": True,
    "login_url": "/login",

    # session config
    "session":{
        "driver": "redis",
        "driver_settings":{
            "host": 'localhost',
            "port": 6379,
            "db": 0,
            "max_connections": 1024,

        },
        "force_persistence": True,
        "cache_driver": True,     # cache driver in application.
        "cookie_config": {
            "expires_days": 7,    # 设置cookie有效期是7天
            "httponly": True      # 设置只在HTTP协议下访问
        }
    },

    # celery config
    "CELERY_RESULT_BACKEND": "redis://localhost:6379/1",
    "CELERY_BROKER_URL": "redis://localhost:6379/0",

    # db config
    'SQLALCHEMY_DATABASE_URI':'postgresql://zeus:newpass@localhost/zeus',

}

# 测试环境
TestingConfig = {
    "debug": True,
    "allow_remote_access": True,
    "template_path": os.path.join(BaseDir, "templates"),
    "static_path": os.path.join(BaseDir, 'static'),
    "log_path" : os.path.join(BaseDir, 'logs'),
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    "xsrf_cookies": True,
    "login_url": "/login",

    # session config
    "session": {
        "driver": "redis",
        "driver_settings":{
            "host": 'localhost',
            "port": 6379,
            "db": 0,
            "max_connections": 1024,

        },
        "force_persistence": True,
        "cache_driver": True,     # cache driver in application.
        "cookie_config": {
            "expires_days": 7,    # 设置cookie有效期是7天
            "httponly": True      # 设置只在HTTP协议下访问
        }
    },

    # celery config
    "CELERY_RESULT_BACKEND": "redis://localhost:6379/1",
    "CELERY_BROKER_URL": "redis://localhost:6379/0"
}


# 生产环境
ProductionConfig = {
    "debug": True,
    "allow_remote_access": True,
    "template_path": os.path.join(BaseDir, "templates"),
    "static_path": os.path.join(BaseDir, 'static'),
    "log_path" : os.path.join(BaseDir, 'logs'),
    "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    "xsrf_cookies": True,
    "login_url": "/login",

    # session config
    "session": {
        "driver": "redis",
        "driver_settings":{
            "host": 'localhost',
            "port": 6379,
            "db": 0,
            "max_connections": 1024,

        },
        "force_persistence": True,
        "cache_driver": True,     # cache driver in application.
        "cookie_config": {
            "expires_days": 7,    # 设置cookie有效期是7天
            "httponly": True      # 设置只在HTTP协议下访问
        }
    },

    # celery config
    "CELERY_RESULT_BACKEND": "redis://localhost:6379/1",
    "CELERY_BROKER_URL": "redis://localhost:6379/0"
}

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


Config = config.get(os.environ.get('CONFIG_NAME', 'default'))

from urls import urls

from db import get_session