#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/17'
"""
import os
import time
# from app import celery
from celery.task import task, periodic_task


@task
def add(x, y):
    time.sleep(5)
    return x + y