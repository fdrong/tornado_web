#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/9'
"""


def login_required(f):
    def _wrapper(self, *args, **kwargs):
        logged = self.current_user
        if logged == None:
            self.write("no login")
            self.finish()
        else:
            f(self, *args, **kwargs)
    return _wrapper