#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/9/30'
"""
import os
import re
import json
import time
import tornado.web
import tornado.log
from tornado.web import HTTPError
from tornado.web import _time_independent_equals
from tornado.web import utf8
from sqlalchemy import func
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import JSONWebSignatureSerializer as Serializer
from app.lib.encrypt import md5_encrypt
from app.lib.decorator import try_except
from app.lib.const import IpWhiteList
from app.models import User
from torndsession.sessionhandler import SessionBaseHandler
from app.tasks import logger


class BaseHandler(SessionBaseHandler):

    def get_current_user(self):
        username = self.session.get("username")
        if not username:
            # for debug
            # if self.get_json('username'):
            #     username = self.get_json('username')
            #     return self.db.query(User).filter(func.lower(User.umname) == func.lower(username)).first()
            return None
        else:
            return self.db.query(User).filter(func.lower(User.umname) == func.lower(username)).first()

    @property
    def logger(self):
        return tornado.log.app_log

    @property
    def db(self):
        return self.application.db

    @try_except
    def get_json(self, name, default=None, required=False, validate=None):
        """
        get a key value from request application/json data
        :param name: the json key
        :param default: if not will set the default value
        :param required: if True and the key is missing, raise missing error
        :param validate: need required=True if validate the re regex will check the pattern if pass or not
        :return: the key'value of application/json data
        """
        if self.request.body:
            data = json.loads(self.request.body)
            value = data.get(name, default)
        else:
            data = self.request.arguments
            value = self.get_argument(name, default)
        if required or validate:
            if name not in data:
                raise Exception(u'参数: %s 缺失!' % name)
            if name in data and (value is None or value == ''):
                raise Exception(u'参数: %s 不能为空' % name)

        if validate:
            pattern = re.compile(validate)
            if not isinstance(value, basestring):
                value = str(value)
            if not pattern.match(value):
                raise Exception(u'请输入正确的%s格式!' % name)

        return value

    # 跨域设置 全局执行任务
    def set_default_headers(self):
        # add csrf
        self.xsrf_form_html()
        # self.set_header('Access-Control-Allow-Origin', '*')
        # self.set_header('Access-Control-Allow-Methods', 'GET, POST, DELETE, PUT, OPTIONS')
        # self.set_header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept,Cache-Control')

    def paginate(self, query):
        '''
        this function is used to paginate the query set
        need the request param page and pageSize
        :return: first is the total of query, second is the querylist of pagination
        '''
        page = self.get_json('page', default=1)
        pageSize = self.get_json('pageSize', default=10)
        querylist = query.limit(pageSize).offset((page - 1) * pageSize).all()
        return query.count(), querylist

    def log_async(self, type, msg, user=None):
        data = dict()
        data["user_id"] = self.current_user.id if self.current_user else user.id
        data["ip"] = self.request.remote_ip
        data["message"] = msg
        data["type"] = type
        logger.delay(**data)

    def check_xsrf_cookie(self):
        """Verifies that the ``_xsrf`` cookie matches the ``_xsrf`` argument.

        To prevent cross-site request forgery, we set an ``_xsrf``
        cookie and include the same value as a non-cookie
        field with all ``POST`` requests. If the two do not match, we
        reject the form submission as a potential forgery.

        The ``_xsrf`` value may be set as either a form field named ``_xsrf``
        or in a custom HTTP header named ``X-XSRFToken`` or ``X-CSRFToken``
        (the latter is accepted for compatibility with Django).

        See http://en.wikipedia.org/wiki/Cross-site_request_forgery

        Prior to release 1.1.1, this check was ignored if the HTTP header
        ``X-Requested-With: XMLHTTPRequest`` was present.  This exception
        has been shown to be insecure and has been removed.  For more
        information please see
        http://www.djangoproject.com/weblog/2011/feb/08/security/
        http://weblog.rubyonrails.org/2011/2/8/csrf-protection-bypass-in-ruby-on-rails

        .. versionchanged:: 3.2.2
           Added support for cookie version 2.  Both versions 1 and 2 are
           supported.
        """
        # IP 白名单略过
        if self.request.remote_ip in IpWhiteList:
            return
        token = (self.get_argument("_xsrf", None) or
                 self.request.headers.get("X-Xsrftoken") or
                 self.request.headers.get("X-Csrftoken"))
        if not token:
            self.write({"code": "4006", "msg": "'_xsrf' argument missing from POST"})
            return self.finish()

        _, token, _ = self._decode_xsrf_token(token)
        _, expected_token, _ = self._get_raw_xsrf_token()
        if not token:
            self.write({"code": "4006", "msg": "'_xsrf' argument has invalid format"})
            return self.finish()
        if not _time_independent_equals(utf8(token), utf8(expected_token)):
            self.write({"code": "4006", "msg": "XSRF cookie does not match POST argument"})
            return self.finish()

    def set_obj_value(self, obj, dict_value):
        for key, value in dict_value.items():
            setattr(obj, key, value)
        return obj

    def generate_time_token(self, jsondata):
        s = Serializer('HEC4ABL3WTUYUZTM')
        return s.dumps(jsondata)

    def decode_time_token(self, token):
        s = Serializer('HEC4ABL3WTUYUZTM')
        try:
            data = s.loads(token)
        except:
            return False
        return data

    def on_finish(self):
        self.db.remove()


class LogFormatter(tornado.log.LogFormatter):
    def __init__(self):
        super(LogFormatter, self).__init__(
            # fmt="%(color)s[%(asctime)s %(filename)s:%(funcName)s:%(lineno)d %(levelname)s]%(end_color)s %(message)s",
            fmt="%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )