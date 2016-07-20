#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.cache import Cache
from . import admin, AdminHandler


class AdminCacheHandler(AdminHandler):
    @admin
    def get(self):
        self.render('admin/cache.html')


class AdminCacheDeleteHandler(AdminHandler):
    @admin
    def post(self):
        try:
            Cache.delete(self.get_argument('exp'), exp=True)
            self.flash(1)
        except:
            self.flash(0)
