#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/25'
"""

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .users import User