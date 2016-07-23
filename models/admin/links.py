#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.base import Base


class Links(Base):
    def __init__(self):
        super(Links, self).__init__()

    def get_links_list(self, limit, offset):
        return self.g_mysql.query("select * from links order by link_id desc limit %s offset %s", limit, offset)

    def get_link_by_id(self, link_id):
        return self.g_mysql.get("select * from links where link_id=%s", link_id)

    def update_link_by_info(self, link_info):
        self.g_mysql.execute("update links set link_name=%s, link_href=%s, link_desp=%s, link_rank=%s, "
                             "link_utms=%s where link_id=%s" % tuple(link_info))

    def insert_link_info(self, link_info):
        self.g_mysql.execute("insert into links(link_name, link_href, link_desp, link_rank, link_ctms, link_utms) "
                             "values('%s', '%s', '%s', '%s', '%s', '%s')" % tuple(link_info))

    def delete_link_by_id(self, link_id, link_utms):
        self.g_mysql.execute("delete from links where link_id=%s and link_utms=%s", link_id, link_utms)

    def get_links_by_rank(self, link_rank):
        return self.g_mysql.query("select * from links where link_rank>=%s order by link_rank desc, "
                                  "link_id desc limit 99", link_rank)

    def get_links(self):
        return self.g_mysql.query("select * from links where link_rank>0 order by link_rank desc, link_id desc")
