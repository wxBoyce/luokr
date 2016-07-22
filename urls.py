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

from handlers.admin.users import AdminUsersHandler, AdminUserHandler, AdminUserCreateHandler

from handlers.admin.files import AdminFilesHandler, AdminFileHandler, AdminFileUploadHandler

from handlers.admin.terms import AdminTermsHandler, AdminTermHandler, AdminTermCreateHandler

from handlers.admin.links import AdminLinksHandler, AdminLinkHandler, AdminLinkCreateHandler, AdminLinkDeleteHandler

from handlers.admin.posts import AdminPostsHandler, AdminPostHiddenHandler, AdminPostCreateHandler


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

    (r'/admin/users', AdminUsersHandler),
    (r'/admin/user', AdminUserHandler),
    (r'/admin/user/create', AdminUserCreateHandler),

    (r'/admin/files', AdminFilesHandler),
    (r'/admin/file', AdminFileHandler),
    (r'/admin/file/upload', AdminFileUploadHandler),

    (r'/admin/terms', AdminTermsHandler),
    (r'/admin/term', AdminTermHandler),
    (r'/admin/term/create', AdminTermCreateHandler),

    (r'/admin/links', AdminLinksHandler),
    (r'/admin/link', AdminLinkHandler),
    (r'/admin/link/create', AdminLinkCreateHandler),
    (r'/admin/link/create', AdminLinkDeleteHandler),

    (r'/admin/posts', AdminPostsHandler),
    (r'/admin/post/hidden', AdminPostHiddenHandler),
    (r'/admin/post/create', AdminPostCreateHandler),
}
