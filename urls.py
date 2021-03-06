#!/usr/bin/env python
# -*- coding: utf-8 -*-


from handlers.posts import PostsHandler, PostHandler

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

from handlers.admin.talks import AdminTalksHandler, AdminTalkHandler, AdminTalkDeleteHandler

from handlers.admin.email import AdminMailsHandler, AdminMailAccessHandler, AdminMailDeleteHandler

from handlers.error import ErrorHandler
from handlers.about import AboutHandler
from handlers.apply import ApplyHandler
from handlers.email import EmailHandler
from handlers.links import LinksHandler
from handlers.score import ScoreHandler
from handlers.voice import VoiceHandler
from handlers.talks import TalksHandler


urls = {
    (r'/', PostsHandler),
    (r'/s', PostsHandler),
    (r'/t/([^/]+)', PostHandler),
    (r'/p/([1-9][0-9]*)', PostHandler),

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

    (r'/admin/talks', AdminTalksHandler),
    (r'/admin/talk', AdminTalkHandler),
    (r'/admin/talk/delete', AdminTalkDeleteHandler),

    (r'/admin/mails', AdminMailsHandler),
    (r'/admin/mail/access', AdminMailAccessHandler),
    (r'/admin/mail/delete', AdminMailDeleteHandler),

    (r'/about', AboutHandler),
    (r'/apply', ApplyHandler),
    (r'/email', EmailHandler),
    (r'/links', LinksHandler),
    (r'/score', ScoreHandler),
    (r'/voice', VoiceHandler),
    (r'/talks(\.json)', TalksHandler),

    # (r'.*', ErrorHandler),

}
