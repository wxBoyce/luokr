#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base


class Posts(Base):

    def __init__(self):
        super(Posts, self).__init__()

    def get_posts_by_user_id(self, query):
        return self.g_mysql.query("select * from posts where user_id='%s' and post_stat>0 and post_ptms<'%s' "
                                  "order by post_ptms desc limit %s offset %s" % tuple(query))

    def get_posts_list(self, limit, offset):
        return self.g_mysql.query("select * from posts order by post_id desc limit %s offset %s", limit, offset)

    def update_post_by_id(self, post_id):
        self.g_mysql.execute("update posts set post_stat=0 where post_id=%s", post_id)

    def get_post_by_id(self, post_id):
        return self.g_mysql.get("select * from posts where post_id=%s", post_id)

    def get_post_terms_by_post_id(self, post_id):
        return self.g_mysql.get("select post_id,term_id from post_terms where post_id = %s", post_id)
