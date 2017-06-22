#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ =''
__author__ = 'fdrong'
__mtime__ = '2016/10/9'
"""


import time
import functools
import traceback
from sqlalchemy.exc import IntegrityError
from app.models import Base


def login_required(method):
    """Decorate methods with this to require that the user be logged in.

    If you configure a login url with a query parameter, Tornado will
    assume you know what you're doing and use it as-is.  If not, it
    will add a `next` parameter so the login page knows where to send
    you once you're logged in.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # check user if logged in
        if not self.current_user:
            return self.write({"code": "4001", "msg": "user is not login"})
        # check if user disabled
        if self.current_user.disable:
            return self.write({"code": "4005", "msg": "user is disabled"})
        # check if user's role has changed
        if self.get_cookie('role') != self.current_user.role.name:
            return self.write({"code": "4002", "msg": "user's role changed"})
        return method(self, *args, **kwargs)
    return wrapper


def permission_required(perm):
    """
    Decorator for views that checks whether a user has a particular permission
    enabled, redirecting to the log-in page if necessary.
    is raised.
    if use permission_required not need the login_required
    """
    def check_perms(user):
        # First check if the user has the permission (even anon users)
        if user.can(perm):
            return True
        else:
            return {"code": "4003", "msg": "Permission denied, permission: %s is needed" % perm}
    return check_user_permission(check_perms)


def check_user_permission(check_func):
    """
    Decorator for views that checks that the user passes the check function,
    redirecting to the log-in page if not login. The check function should be a callable
    that takes the user object and returns True if the user passes.
    """

    def decorator(method):
        @functools.wraps(method)
        def _wrapped_view(self, *args, **kwargs):
            # check user if logged in
            if not self.current_user:
                return self.write({"code": "4001", "msg": "user is not login"})
            # check if user disabled
            if self.current_user.disable:
                return self.write({"code": "4005", "msg": "user is disabled"})
            # check if user's role has changed
            if self.get_cookie('role') != self.current_user.role.name:
                return self.write({"code": "4002", "msg": "user's role changed"})
            # check user if has the permission
            perm_checked = check_func(self.current_user)
            if perm_checked is True:
                return method(self, *args, **kwargs)
            else:
                return self.write(perm_checked)
        return _wrapped_view
    return decorator


# catch the exception of the interface function
def try_except(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        # 处理key dumplicated
        except IntegrityError as e:
            column = e.orig.diag.constraint_name.split('_')[-2]
            table_name = e.orig.diag.table_name
            column_doc = Base.metadata.tables.get(table_name).columns.get(column).doc
            msg = u"{}已存在,保存失败!".format(column_doc)
        except KeyError as e:
            msg = "Key Error : %s" % e.message
        except Exception as e:
            msg = "%s" % e.message
        traceback.print_exc()
        self.logger.error(msg)
        self.db.rollback()
        self.write(
            {
                "msg": msg,
                "code": "1001"

            }
        )
        return self.finish()
    return wrapper


# figure out the time of the interface function cost
def timeit(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        start = time.time()
        func(self, *args, **kwargs)
        end = time.time()
        self.logger.info("time spend: %d" % (end - start))
    return wrapper