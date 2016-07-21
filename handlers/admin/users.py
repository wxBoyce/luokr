#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from . import admin, AdminHandler

from utils.tools import Tools


class AdminUsersHandler(AdminHandler):
    @admin
    def get(self):
        pager = {}
        pager['qnty'] = min(max(int(self.get_argument('qnty', 10)), 1), 100)
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        users = self.users_ins.get_user_info_list(pager['qnty'], (pager['page']-1)*pager['qnty'])

        if users:
            pager['lgth'] = len(users)

        self.render('admin/users.html', users=users, pager=pager)


class AdminUserHandler(AdminHandler):
    @admin
    def get(self):
        user = self.users_ins.get_user_by_id(self.get_argument('user_id'))
        if not user:
            self.flash(0, {'sta': 404})
            return

        self.render('admin/user.html', user=user)

    @admin
    def post(self):
        user = self.users_ins.get_user_by_id(self.get_argument('user_id'))
        if not user:
            self.flash(0, {'sta': 404})
            return

        if user['user_id'] == self.current_user['user_id']:
            self.flash(0, {'sta': 403})
            return

        try:
            user_mail = self.get_argument('user_mail')
            user_sign = self.get_argument('user_sign')
            user_logo = self.get_argument('user_logo')
            user_meta = self.get_argument('user_meta')
            user_perm = self.get_argument('user_perm')
            user_pswd = self.get_argument('user_pswd', '')
            user_rpwd = self.get_argument('user_rpwd', '')
            user_perm = int(user_perm) & int(self.current_user['user_perm']) & 0x7FFFFFFF

            if user_pswd != user_rpwd:
                self.flash(0, {'msg': '确认密码不匹配'})
                return

            if not (len(user_pswd) >= 6):
                self.flash(0, {'msg': '无效的用户密码'})
                return

            if not Tools.chk_is_user_mail(user_mail):
                self.flash(0, {'msg': '无效的用户邮箱'})
                return

            if user_mail != user['user_mail'] and self.users_ins.get_user_by_mail(user_mail):
                self.flash(0, {'msg': '用户邮箱已经存在'})
                return

            if user_pswd:
                user_auid = Tools.generate_randauid()
                user_salt = Tools.generate_randsalt()
                user_pswd = Tools.generate_password(user_pswd, user_salt)
                self.users_ins.update_user_info_by_pwd([user_auid, user_mail, user_sign, user_logo, user_meta,
                                                        user_pswd, user_salt, user_perm, int(time.time()),
                                                        int(time.time()), user['user_id']])
            else:
                self.users_ins.update_user_info_by_other([user_mail, user_sign, user_logo, user_meta, user_perm,
                                                          int(time.time()), user['user_id']])
            self.ualog(self.current_user, u"更新用户：" + str(user['user_id']), user['user_name'])
            self.flash(1)
            return
        except:
            pass
        self.flash(0)


class AdminUserCreateHandler(AdminHandler):
    @admin
    def get(self):
        self.render('admin/user-create.html')

    @admin
    def post(self):
        try:
            user_name = self.get_argument('user_name')
            user_mail = self.get_argument('user_mail')
            user_perm = self.get_argument('user_perm')
            user_pswd = self.get_argument('user_pswd')
            user_rpwd = self.get_argument('user_rpwd')
            user_sign = self.get_argument('user_sign', '')
            user_logo = self.get_argument('user_logo', '')
            user_meta = self.get_argument('user_meta', '')
            user_ctms = int(time.time())
            user_utms = user_ctms
            user_atms = user_ctms

            if len(user_name) < 3 or not Tools.chk_is_user_name(user_name):
                self.flash(0, {'msg': '无效的用户帐号'})
                return

            if len(user_pswd) < 6 or (user_pswd != user_rpwd):
                self.flash(0, {'msg': '无效的用户密码'})
                return

            if len(user_mail) < 3 or not Tools.chk_is_user_mail(user_mail):
                self.flash(0, {'msg': '无效的用户邮箱'})
                return

            if self.users_ins.get_user_by_name(user_name):
                self.flash(0, {'msg': '用户帐号已存在'})
                return

            if self.users_ins.get_user_by_mail(user_mail):
                self.flash(0, {'msg': '用户邮箱已存在'})
                return

            user_auid = Tools.generate_randauid()
            user_salt = Tools.generate_randsalt()
            user_pswd = Tools.generate_password(user_rpwd, user_salt)
            user_perm = int(user_perm) & 0x7FFFFFFF

            self.users_ins.insert_new_user([user_auid, user_name, user_salt, user_pswd, user_perm, user_mail,
                                            user_sign, user_logo, user_meta, user_ctms, user_utms, user_atms])

            self.ualog(self.current_user, u"新增用户：", user_name)
            self.flash(1)
            return
        except:
            pass
        self.flash(0)
