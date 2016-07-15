#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base


class Posts(Base):

    def __init__(self):
        super(Posts, self).__init__()

    def get_posts_by_user_id(self, query):
        return self.g_mysql.query("select * from posts where user_id='%s' and post_stat>0 and post_ptms<'%s' "
                                  "order by post_ptms desc limit %s offset %s" % tuple(query))

