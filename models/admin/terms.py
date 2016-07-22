#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.base import Base


class Terms(Base):
    def __init__(self):
        super(Terms, self).__init__()

    def get_terms_list(self, limit, offset):
        return self.g_mysql.query("select * from terms order by term_id desc limit %s offset %s", limit, offset)

    def get_term_by_id(self, term_id):
        return self.g_mysql.get("select * from terms where term_id = %s", term_id)

    def update_term_name_by_id(self, term_name, term_id):
        self.g_mysql.execute("update terms set term_name = %s where term_id = %s" % (term_name, term_id))

    def get_terms_info(self):
        return self.g_mysql.query("select * from terms order by term_id desc, term_refc desc limit 9")

    def get_term_by_name(self, term_name):
        return self.g_mysql.get("select term_id from terms where term_name = %s", term_name)

    def get_terms_by_ids(self, ids):
        return self.g_mysql.query("select * from terms where term_id in (%s)" % ids)
