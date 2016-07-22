#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from utils.util import Utils

from . import admin, AdminHandler


class AdminPostsHandler(AdminHandler):
    @admin
    def get(self):
        pager = {}
        pager['qnty'] = min(max(int(self.get_argument('qnty', 10)), 1), 100)
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        posts = self.posts_ins.get_posts_list(pager['qnty'], (pager['page']-1)*pager['qnty'])

        psers = {}
        if posts:
            pager['lgth'] = len(posts)
            psers = Utils.array_keyto(self.users_ins.get_posts_user(','.join(str(i['user_id']) for i in posts)))

        self.render('admin/posts.html', pager=pager, posts=posts, psers=psers)


class AdminPostHiddenHandler(AdminHandler):
    @admin
    def post(self):
        try:
            post_id = self.get_argument('post_id')
            self.posts_ins.update_post_by_id(post_id)
            self.flash(1)
        except:
            self.flash(0)


class AdminPostCreateHandler(AdminHandler):
    @admin
    def get(self):
        mode = self.get_argument('mode', None)
        terms = self.terms_ins.get_terms_info()

        self.render('admin/post-create.html', mode=mode, terms=terms)

    @admin
    def post(self):
        try:
            post_title = self.get_argument('post_title')
            post_descp = self.get_argument('post_descp')
            post_author = self.get_argument('post_author')
            post_source = self.get_argument('post_source')
            post_summary = self.get_argument('post_summary')
            post_content = self.get_argument('post_content')

            post_rank = int(self.get_argument('post_rank'))
            post_stat = int(self.get_argument('post_stat', 0))
            post_ptms = int(time.mktime(time.strptime(self.get_argument('post_ptms'), '%Y-%m-%d %H:%M:%S')))
            post_ctms = int(time.time())
            post_utms = post_ctms

            term_list = []
            for term_name in self.get_argument('term_list').split(' '):
                if term_name == '':
                    continue
                term_list.append(term_name)

            if len(term_list) > 10:
                self.flash(0, {'msg': '标签数量限制不能超过 10 个'})
                return

            term_imap = {}
            term_ctms = int(time.time())
            for term_name in term_list:
                term_id = self.terms_ins.get_term_by_name(term_name)
                if term_id:
                    term_id = term_id['term_id']
                else:
                    # term_id = self.datum('terms').invoke('insert or ignore into terms (term_name, term_ctms) values (?, ?)', (term_name, term_ctms,)).lastrowid
                    term_id = 1
                if term_id:
                    term_imap[term_id] = term_name

                # post_id = self.datum('posts').invoke('insert into posts (user_id, post_title, post_descp, post_author, post_source, post_summary, post_content,post_stat, post_rank, post_ptms, post_ctms, post_utms) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (self.current_user['user_id'], post_title, post_descp, post_author, post_source, post_summary, post_content, post_stat, post_rank, post_ptms, post_ctms, post_utms,)).lastrowid
                post_id = None

                if term_imap:
                    for term_id in term_imap:
                        # self.datum('posts').invoke('insert or ignore into post_terms (post_id, term_id) values (' + str(post_id) + ',' + str(term_id) + ')')
                        pass
                if term_imap:
                    # self.datum('terms').invoke('update terms set term_refc = term_refc + 1 where term_id in (' + ','.join([str(i) for i in term_imap.keys()]) + ')')
                    pass

                self.ualog(self.current_user, u'新增文章：' + str(post_id))
                self.flash(1, {'url': '/admin/post?post_id=' + str(post_id)})
        except:
            self.flash(0)


class AdminPostHandler(AdminHandler):
    @admin
    def get(self):
        post_id = self.get_argument('post_id')
        post = self.posts_ins.get_post_by_id(post_id)
        if not post:
            self.flash(0, {'sta': 404})
            return
        mode = self.get_argument('mode', None)
        terms = self.terms_ins.get_terms_info()
        ptids = self.posts_ins.get_post_terms_by_post_id(post_id)
        ptags = {}
        if ptids:
            ptags = self.terms_ins.get_terms_by_ids(','.join(str(i['term_id']) for i in ptids))
            if ptags:
                ptids = Utils.array_group(ptids, 'post_id')
                ptags = Utils.array_keyto(ptags, 'term_id')

        self.render('admin/post.html', mode=mode, post=post, terms=terms, ptids=ptids, ptags=ptags)

    @admin
    def post(self):
        pass
