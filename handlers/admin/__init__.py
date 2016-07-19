#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

from utils.tools import Tools

from handlers.base import BaseHandler, login


class AdminHandler(BaseHandler):
    pass


def admin(method):
    @login
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if Tools.chk_user_is_root(self.current_user):
            return method(self, *args, **kwargs)
        else:
            self.flash(0, {'sta': 403, 'url': self.get_login_url()})
            return

    return wrapper
