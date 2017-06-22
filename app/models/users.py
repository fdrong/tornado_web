#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/25'
"""

import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy_utils import PasswordType, URLType

from app.models import Base


class User(Base):
    """
        users model
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, name='id')
    username = Column(String(60), nullable=False, name='username')
    password = Column(String(500), nullable=False, name='password')
    first_name = Column(
        String(60), nullable=True, name='first_name', default=''
    )
    last_name = Column(
        String(60), nullable=True, name='last_name', default=''
    )
    email = Column(String(60), nullable=True, default='', name='email')
    avatar = Column(URLType, nullable=True, default=None, name='avatar')

    last_login_time = Column(DateTime(
        timezone=False), nullable=True, name='last_login_time'
    )
    last_opt_time = Column(DateTime(
        timezone=False), nullable=True, name='last_opt_time'
    )
    otp_request_count = Column(Integer, nullable=False, default=0)

    create_at = Column(DateTime(
        timezone=False), default=datetime.datetime.now, name='create_at'
    )
    update_at = Column(DateTime(
        timezone=False), onupdate=datetime.datetime.now, default=datetime.datetime.now, name='update_at'
    )

    @property
    def as_dict(self):
        """
            object to dict
        """
        return {
            column.name: str(getattr(self, column.name))
            for column in self.__table__.columns if column.name != 'password'
        }

    @property
    def flats(self):
        """
            get all flats belong to user
        """
        return []

    @property
    def display_name(self):
        """
            pretty user name
        """
        return ('{} {}'.format(self.first_name, self.first_name)
                if self.first_name and self.last_name else self.username)

    def can(self, permission):
        """
        check the object if has the permission
        if yes return True
        else return false
        """
        if permission in [item.name for item in self.role.permissions]:
            return True
        else:
            return False

