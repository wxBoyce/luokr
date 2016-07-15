#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from . import ShellHandler


class Shell_IndexHandler(ShellHandler):

    def get(self, name):
        s_time = int(time.time())
        pager = dict()
        pager['qnty'] = 5
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        user = self.users_ins.get_user_by_name(name)
        if not user:
            self.flash(0, {'sta': 404})
            return

        # 获取当前用户的博文
        posts = self.posts_ins.get_posts_by_user_id([user['user_id'], s_time, pager['qnty'], (pager['page']-1)*pager['qnty']])
        if posts:
            pager['lgth'] = len(posts)

        if self.get_argument('_pjax', None) == '#shell-index-posts':
            self.render('shell/index/posts.html', user=user, pager=pager, posts=posts)
            return

        self.render('shell/index.html', user=user, pager=pager, posts=posts)
