#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/11/18'
"""

import datetime
from sqlalchemy import Column, Integer, String, DateTime

from app.models import Base


class Permission(Base):
    """
        permission model
    """
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, autoincrement=True, name='id')

    name = Column(String(100), nullable=False, name='name')
    codename = Column(String(100), nullable=False, name='codename')
    desc = Column(String(200), nullable=True, default=None, name='desc')

    create_at = Column(DateTime(
        timezone=False), default=datetime.datetime.now, name='create_at'
    )
    update_at = Column(DateTime(
        timezone=False), onupdate=datetime.datetime.now, default=datetime.datetime.now, name='update_at'
    )

    # date_joined = Column(DateTime(
    #     timezone=False), default=datetime.datetime.now, name='date_joined'
    # )

    # avatar = Column(URLType, nullable=True, default=None, name='avatar')

    @property
    def as_dict(self):
        """
            object to dict
        """
        return {
            column.name: str(getattr(self, column.name))
            for column in self.__table__.columns
        }