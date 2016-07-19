#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import admin, AdminHandler


class AdminAlogsHandler(AdminHandler):
    @admin
    def get(self):
        pager ={}
        pager['qnty'] = min(max(int(self.get_argument('qnty', 10)), 1), 100)
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        alogs = self.admin_ins.get_alogs(pager['qnty'], (pager['page']-1)*pager['qnty'])

        if alogs:
            pager['lgth'] = len(alogs)

        self.render('admin/alogs.html', alogs=alogs, pager=pager)
