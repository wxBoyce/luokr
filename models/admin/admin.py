#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
