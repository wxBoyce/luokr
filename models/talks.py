#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base


class Talks(Base):
    def __init__(self):
        super(Talks, self).__init__()

    def get_talks_list(self, limit, offset):
        return self.g_mysql.query("select * from talks order by talk_id limit %s offset %s", limit, offset)

    def get_talk_by_id(self, talk_id):
        return self.g_mysql.get("select * from talks where talk_id=%s", talk_id)

    def update_talk_by_id(self, talk_info):
        self.g_mysql.execute("update talks set user_name='%s', user_mail='%s', talk_rank=%s+talk_plus-talk_mins, "
                             "talk_text='%s', talk_utms='%s' where talk_id=%s" % tuple(talk_info))

    def delete_talk_by_id(self, talk_id, talk_ctms):
        self.g_mysql.execute("delete from talks where talk_id=%s and talk_ctms=%s", talk_id, talk_ctms)
