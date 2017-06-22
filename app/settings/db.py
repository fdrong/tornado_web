#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/25'
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from . import Config
from multiprocessing.util import register_after_fork


def get_session(base):
    """
    :param base: sqlachemy base class
    :return: sqlalchemy scoped session
    """
    if base:
        engine = create_engine(Config.get('SQLALCHEMY_DATABASE_URI'))
        base.metadata.create_all(bind=engine)
        # register_after_fork(engine, engine.dispose())
        return scoped_session(sessionmaker(bind=engine))