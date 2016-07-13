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
