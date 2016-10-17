#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/17'
"""
import os
import time
from celery import Celery, platforms
from settings import config
# from celery.task import task, periodic_task

# celery config
config_dict = config.get(os.environ.get('CONFIG_NAME', 'default'))
celery = Celery('celery', backend=config_dict['CELERY_RESULT_BACKEND'], broker=config_dict['CELERY_BROKER_URL'])
platforms.C_FORCE_ROOT = True  # 在ROOT下启动4


@celery.task
def add(x, y):
    time.sleep(5)
    return x + y