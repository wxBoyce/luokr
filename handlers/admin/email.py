#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from . import admin, AdminHandler


class AdminMailsHandler(AdminHandler):
    @admin
    def get(self):
        pager = {}
        pager['qnty'] = min(max(int(self.get_argument('qnty', 10)), 1), 100)
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        mails = self.email_ins.get_email_list(pager['qnty'], (pager['page']-1)*pager['qnty'])
        if mails:
            pager['lgth'] = len(mails)

        self.render('admin/mails.html', pager=pager, mails=mails)


class AdminMailAccessHandler(AdminHandler):
    @admin
    def post(self):
        try:
            mail_id = self.get_argument('mail_id')
            self.email_ins.update_mail_by_id(mail_id, int(time.time()))
            self.flash(1)
            return
        except:
            pass
        self.flash(0)


class AdminMailDeleteHandler(AdminHandler):
    @admin
    def post(self):
        try:
            mail_id = self.get_argument('mail_id')
            mail_utms = self.get_argument('mail_utms')
            self.email_ins.delete_mail_by_id(mail_id, mail_utms)
            self.ualog(self.current_user, u'删除留言：' + str(mail_id))
            self.flash(1)
            return
        except:
            pass
        self.flash(0)
