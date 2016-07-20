#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from models.base import Base


class Admin(Base):
    def __init__(self):
        super(Admin, self).__init__()

    def get_talks(self):
        return self.g_mysql.query("select * from talks order by talk_id desc limit 3")

    def get_mails(self):
        return self.g_mysql.query("select * from mails order by mail_id desc limit 3")

    def get_alogs(self, limit, offset):
        return self.g_mysql.query("select * from alogs order by alog_id desc limit %s offset %s" % (limit, offset))

    def insert_alogs(self, alog_text, alog_data='', user_ip='', user_id=0, user_name=''):
        sql = "insert into alogs (user_ip, user_id, user_name, alog_text, alog_data, alog_ctms) values ('%s', '%s', '%s', '%s', '%s', %s)" % \
              (user_ip, user_id, user_name, alog_text, alog_data, int(time.time()))
        self.g_mysql.execute(sql)
