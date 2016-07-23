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

    def get_post_list_by_terms(self, term_id, post_ptms, limit, offset):
        return self.g_mysql.query("select posts.* from posts,post_terms where posts.post_id=post_terms.post_id and "
                                  "term_id=%s and post_stat>0 and post_ptms<%s order by post_ptms desc "
                                  "limit %s offset %s", term_id, post_ptms, limit, offset)

    def get_post_list_by_like(self, post_ptms, query, limit, offset):
        return self.g_mysql.query("select * from posts where post_stat>0 and post_ptms<%s and (post_title like %s "
                                  "or post_content like %s) order by post_ptms desc limit %s offset %s", post_ptms, query, query, limit, offset)

    def get_post_list_order_by_time(self, post_ptms, limit, offset):
        return self.g_mysql.query("select * from posts where post_stat>0 and post_ptms<%s order by post_ptms desc "
                                  "limit %s offset %s", post_ptms, limit, offset)

    def get_top_posts(self, stime, confs):
        return self.g_mysql.query("select post_id,post_title,post_descp from posts where post_stat>0 and post_ptms<%s "
                                  "and post_rank>=%s order by post_rank desc, post_id desc limit 9", stime, confs)

    def get_hot_posts(self, stime):
        return self.g_mysql.query("select post_id,post_title,post_descp from posts where post_stat>0 and post_ptms<%s "
                                  "order by post_refc desc, post_id desc limit 9", stime)

    def get_new_posts(self, stime):
        return self.g_mysql.query("select post_id,post_title,post_descp from posts where post_stat>0 and post_ptms<%s "
                                  "order by post_ptms desc, post_id desc limit 9", stime)

    def get_pre_post_id(self, stime, post_id):
        return self.g_mysql.query("select post_id from posts where post_stat>0 and post_ptms<%s and post_id>%s "
                                  "order by post_id asc limit 1", stime, post_id)

    def get_next_post_id(self, stime, post_id):
        return self.g_mysql.query("select post_id from posts where post_stat>0 and post_ptms<%s and post_id>%s "
                                  "order by post_id asc limit 1", stime, post_id)

    def get_rel_posts(self, post_ids, stime):
        return self.g_mysql.query("select post_id,post_title,post_descp from posts where post_stat>0 and post_ptms<%s "
                                  "and post_id in (%s) order by post_ptms desc, post_id desc limit 9", stime, post_ids)
