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
