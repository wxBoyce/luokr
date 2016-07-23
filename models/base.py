#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dbmanage import g_mysql


class Base(object):

    def __init__(self):
        super(Base, self).__init__()
        self.g_mysql = g_mysql

    def get_post_terms_by_post_id(self, ids):
        return self.g_mysql.query("select post_id,term_id from post_terms where post_id in (%s)")

    def get_post_terms_by_id_in_ids(self, post_id, ids):
        return self.g_mysql.query("select distinct post_id from post_terms where post_id<>%s and term_id in (%s) "
                                  "order by term_id desc limit 9", post_id, ids)
