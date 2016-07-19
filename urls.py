#!/usr/bin/env python
# -*- coding: utf-8 -*-


from handlers.test import TestHandler

from handlers.login import LoginHandler
from handlers.leave import LeaveHandler
from handlers.check import CheckHandler

from handlers.shell.panel import ShellPanelHandler
from handlers.shell.index import Shell_IndexHandler

from handlers.admin.index import AdminIndexHandler
from handlers.admin.alogs import AdminAlogsHandler


urls = {
    (r'/', TestHandler),

    (r'/check(\.jpeg)', CheckHandler),
    (r'/login', LoginHandler),
    (r'/leave', LeaveHandler),

    (r'/shell', ShellPanelHandler),
    (r'/@([^/]+)', Shell_IndexHandler),

    (r'/admin', AdminIndexHandler),

    (r'/admin/alogs', AdminAlogsHandler),
}
