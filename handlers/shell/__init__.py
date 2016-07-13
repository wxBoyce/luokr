#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

from handlers.base import BaseHandler, alive


class ShellHandler(BaseHandler):
    pass


def shell(method):
    @alive
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        return method(self, *args, **kwargs)

    return wrapper
