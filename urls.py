#!/usr/bin/env python
# -*- coding: utf-8 -*-


from handlers.test import TestHandler

from handlers.login import LoginHandler


urls = {
    (r'/', TestHandler),

    (r'/login', LoginHandler),
}
