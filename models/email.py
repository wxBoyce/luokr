#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base


class Email(Base):
    def __init__(self):
        super(Email, self).__init__()

    def get_email_list(self, limit, offset):
        return self.g_mysql.query("select * from mails order by mail_id desc limit %s offset %s", limit, offset)

    def update_mail_by_id(self, mail_id, mail_utms):
        self.g_mysql.execute('update mails set mail_stat=1, mail_utms=%s where mail_id=%s', mail_utms, mail_id)

    def delete_mail_by_id(self, mail_id, mail_utms):
        self.g_mysql.execute("delete from mails where mail_id=%s and mail_utms=%s", mail_id, mail_utms)
