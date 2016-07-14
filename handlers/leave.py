#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler, login


class LeaveHandler(BaseHandler):
    @login
    def get(self):
        self.render('leave.html')

    @login
    def post(self):
        self.del_current_sess()
        self.redirect('/login')
