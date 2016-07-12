#!/usr/bin/env python
# -*- coding: utf-8 -*-


from base import BaseHandler


class LoginHandler(BaseHandler):

    def get(self):
        self.render('login.html', next=self.get_argument('next', '/shell'))

    def post(self):
        if self.human_valid():
            self.flash(0, {'msg': '验证码错误!'})
            return

        try:
            username = self.get_argument('username')
            password = self.get_argument('password')
            remember = self.get_argument('remember', None)
            redirect = self.get_argument('redirect', '/shell')

            if remember:
                remember = int(remember)

            user = self.users_ins.get_user_by_name(username)
            print user

        except:
            pass

        self.flash(0, {'msg': '用户名或者密码错误!'})