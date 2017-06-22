#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'rongfudi636'
__mtime__ = '22/06/2017'
"""


import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL, Float, TEXT

from app.models import Base


class Log(Base):
    """
        Log model
    """
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True, name='id')

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, name='user_id')
    type = Column(String(200), nullable=False, name='type')  # 操作类型
    ip = Column(String(40), nullable=True, name='ip')  # 远程主机IP
    message = Column(TEXT, nullable=False, name='message')  # 操作信息
    create_at = Column(DateTime(
        timezone=False), default=datetime.datetime.now, name='create_at'
    )     # 创建时间

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