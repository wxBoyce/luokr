#!/usr/bin/env python
# -*- coding: utf-8 -*-


from base import BaseHandler


class LoginHandler(BaseHandler):

    def get(self):
        self.render('login.html', next=self.get_argument('next', '/shell'))

    def post(self):
        pass