#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/25'
"""


from celery import Celery, platforms
from app.settings import Config
celery = Celery('celery', backend=Config['CELERY_RESULT_BACKEND'], broker=Config['CELERY_BROKER_URL'])
platforms.C_FORCE_ROOT = True  # 在ROOT下启动4

from tasks import add