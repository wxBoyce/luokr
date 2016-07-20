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

from handlers.admin.cache import AdminCacheHandler, AdminCacheDeleteHandler

from handlers.admin.confs import AdminConfsHandler, AdminConfCreateHandler, AdminConfHandler, AdminConfDeleteHandler


urls = {
    (r'/', TestHandler),

    (r'/check(\.jpeg)', CheckHandler),
    (r'/login', LoginHandler),
    (r'/leave', LeaveHandler),

    (r'/shell', ShellPanelHandler),
    (r'/@([^/]+)', Shell_IndexHandler),

    (r'/admin', AdminIndexHandler),

    (r'/admin/alogs', AdminAlogsHandler),

    (r'/admin/cache', AdminCacheHandler),
    (r'/admin/cache/delete', AdminCacheDeleteHandler),

    (r'/admin/confs', AdminConfsHandler),
    (r'/admin/conf', AdminConfHandler),
    (r'/admin/conf/create', AdminConfCreateHandler),
    (r'/admin/conf/delete', AdminConfDeleteHandler),
}
