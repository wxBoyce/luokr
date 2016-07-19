#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import admin, AdminHandler


class AdminIndexHandler(AdminHandler):
    @admin
    def get(self):
        talks = self.admin_ins.get_talks()
        mails = self.admin_ins.get_mails()

        self.render('admin/index.html', talks=talks, mails=mails)
