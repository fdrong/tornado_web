#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '22/06/2017'
"""

import os
import time
# from app import celery
from celery.task import task, periodic_task
from datetime import datetime
from app.models import Log
from app.models import Base as DbBase

from app.settings.db import get_session

session = get_session(DbBase)


# 异步记录日志，提高系统并发效率
@task
def logger(**kwargs):
    if all([kwargs.keys()]):
        log = Log(**kwargs)
        try:    # 存储日志
            session.add(log)
            session.commit()
        except Exception as e:  # 出现异常时，记录到log文件中
            print("Log into database error, reason: %s" % e)
            session.rollback()