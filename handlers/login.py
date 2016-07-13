#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from base import BaseHandler
from utils.tools import Tools


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

            if user and self.entry('login:user#' + str(user['user_id'])):
                self.flash(0, {'msg': '操作太频繁，请稍后再试', 'sta': 429})
                return
            print Tools.generate_password(password, user['user_salt'])
            if user and Tools.generate_password(password, user['user_salt']) == user['user_pswd']:
                self.set_current_sess(user, days=remember)

                logging.info("Current Login: %s" % user['user_id'])

                self.flash(1, {'url': redirect})
                return

        except:
            pass

        self.flash(0, {'msg': '用户名或者密码错误!'})