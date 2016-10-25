#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '16/9/30'
"""
import tornado.web
from app.api import BaseHandler


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        # self.set_secure_cookie("username", self.get_argument("username"), httponly=True, secure=True)
        self.set_secure_cookie("username", self.get_argument("username"))
        self.redirect('/')


class WelcomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('index.html', user=self.current_user)


class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("username")
        self.redirect("/")