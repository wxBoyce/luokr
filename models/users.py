#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base


class Users(Base):

    def __init__(self):
        super(Users, self).__init__()

    def get_user_by_name(self, name):
        return self.g_mysql.get("select * from users where user_name = %s", name)

    def get_user_by_id(self, user_id):
        return self.g_mysql.get("select * from users where user_id = %s", user_id)

    def get_user_by_mail(self, mail):
        return self.g_mysql.get("select * from users where user_mail = %s", mail)

    def update_user_info_by_pwd(self, user_infos):
        self.g_mysql.execute("update users set user_auid='%s', user_mail='%s', user_logo='%s', user_sign='%s',"
                             " user_meta='%s', user_pswd='%s', user_salt='%s', user_atms='%s', user_utms='%s' where "
                             "user_id='%s'" % tuple(user_infos))

    def update_user_info_by_other(self, user_infos):
        self.g_mysql.execute("update users set user_mail='%s', user_logo='%s', user_sign='%s', user_meta='%s', "
                             "user_utms='%s' where user_id='%s'" % tuple(user_infos))

    def get_user_info_list(self, limit, offset):
        return self.g_mysql.query("select * from users order by user_id desc limit %s offset %s", limit, offset)

    def insert_new_user(self, user_info):
        self.g_mysql.execute("insert into users(user_auid, user_name, user_salt, user_pswd, user_perm, user_mail, "
                             "user_sign, user_logo, user_meta, user_ctms, user_utms, user_atms) values('%s', '%s', '%s',"
                             " '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % tuple(user_info))

    def get_posts_user(self, users):
        return self.g_mysql.execute("select * from users where user_id in (%s)" % users)

