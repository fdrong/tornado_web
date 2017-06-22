#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/11/18'
"""


import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from app.models import Base


class UserRole(Base):
    """
        user_role model
    """
    __tablename__ = 'user_role'

    id = Column(Integer, primary_key=True, autoincrement=True, name='id')

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, name='user_id')
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False, name='role_id')

    create_at = Column(DateTime(
        timezone=False), default=datetime.datetime.now, name='create_at'
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