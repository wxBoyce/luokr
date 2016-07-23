#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from utils.util import Utils
from base import BaseHandler


class PostsHandler(BaseHandler):

    def get(self, _tnm=None):
        pager = {}
        pager['qnty'] = 5
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        s_time = int(time.time())
        track = ''

        _qry = self.get_argument('q', None)
        _top = False
        _tag = None

        if _tnm:
            _tag = self.terms_ins.get_term_info_by_name(str(_tnm))

        if _tag:
            posts = self.posts_ins.get_post_list_by_terms(_tag['term_id'], s_time, pager['qnty'], (pager['page']-1)*pager['qnty'])
            track = u'标签：' + _tag['term_name']
        elif _tnm:
            self.flash(0, {'sta': 404})
            return
        elif _qry:
            posts = self.posts_ins.get_post_list_by_like(s_time, '%'+_qry+'%', '%'+_qry+'%', pager['qnty'], (pager['page']-1)*pager['qnty'])
            track = u'搜索：' + _qry
        else:
            posts = self.posts_ins.get_post_list_order_by_time(s_time, pager['qnty'], (pager['page']-1)*pager['qnty'])
            if self.get_argument('page', None) is None:
                _top = True

        ptids = {}
        ptags = {}
        psers = {}
        if posts:
            pager['lgth'] = len(posts)
            ptids = self.posts_ins.get_post_terms_by_post_id(','.join(str(i['post_id']) for i in posts))
            if ptids:
                ptags = Utils.array_keyto(self.terms_ins.get_terms_by_ids(','.join(str(i['post_id']) for i in posts)))
            ptids = Utils.array_group(ptids, 'post_id')
            psers = Utils.array_keyto(self.users_ins.get_posts_user(','.join(str(i['user_id']) for i in posts)))

        keyws_tag = self.terms_ins.get_terms_to_post()
        posts_top = self.posts_ins.get_top_posts(s_time, self.get_runtime_conf('index_posts_top_rank'))
        posts_hot = self.posts_ins.get_hot_posts(s_time)
        posts_new = self.posts_ins.get_new_posts(s_time)
        posts_rel = []
        talks_new = self.talks_ins.get_new_talks(self.get_runtime_conf('posts_talks_min_rank'))

        if _top:
            links_top = self.links_ins.get_links_by_rank(self.get_runtime_conf('index_links_min_rank'))
        else:
            links_top = None

        slabs_top = self.jsons(self.get_runtime_conf('slabs'))

        self.render('posts.html', track=track, pager=pager, posts=posts, psers=psers, ptids=ptids, ptags=ptags,
                    posts_top=posts_top, posts_hot=posts_hot, posts_new=posts_new, posts_rel=posts_rel,
                    slabs_top=slabs_top, keyws_tag=keyws_tag, talks_new=talks_new, links_top=links_top)


class PostHandler(BaseHandler):
    def get(self, post_id):
        s_time = int(time.time())

        post = self.posts_ins.get_post_by_id(post_id)
        if not post or ((not self.get_current_user()) and (not post['post_stat'] or post['post_ptms'] >= s_time)):
            self.flash(0, {'sta': 404})
            return

        ptids = {}
        ptags = {}
        psers = {}

        ptids = self.posts_ins.get_post_terms_by_post_id(post_id)
        if ptids:
            ptags = Utils.array_keyto(self.terms_ins.get_terms_by_ids(','.join(str(i['term_id']) for i in ptids)))
        ptids = Utils.array_group(ptids, 'post_id')
        psers = Utils.array_keyto(self.users_ins.get_user_by_id(post['user_id']))

        post_prev = self.posts_ins.get_pre_post_id(s_time, post_id)
        if post_prev:
            post_prev = post_prev['post_id']
        else:
            post_post_prev = 0

        post_next = self.posts_ins.get_next_post_id(s_time, post_id)
        if post_next:
            post_next = post_next['post_id']
        else:
            post_next = 0

        posts_top = self.posts_ins.get_top_posts(s_time, self.get_runtime_conf('index_posts_top_rank'))
        posts_hot = self.posts_ins.get_hot_posts(s_time)
        posts_new = self.posts_ins.get_new_posts(s_time)
        posts_rel = []

        if post['post_id'] in ptids:
            poids = self.posts_ins.get_post_terms_by_id_in_ids(post['post_id'], ','.join(str(i['term_id']) for i in ptids[post['post_id']]))
            if poids:
                posts_rel = self.posts_ins.get_rel_posts(','.join(str(i['post_id']) for i in poids), s_time)

        keyws_tag = self.terms_ins.get_terms_to_post()

        talks = []
        talks_new = []

        slabs_top = self.jsons(self.get_runtime_conf('slabs'))

        links_top = None

        self.render('index/post.html', post=post, psers=psers, ptids=ptids, ptags=ptags, talks=talks,
                    post_prev=post_prev, post_next=post_next, posts_top=posts_top, posts_hot=posts_hot,
                    posts_new=posts_new, posts_rel=posts_rel, slabs_top=slabs_top, keyws_tag=keyws_tag,
                    talks_new=talks_new, links_top=links_top)
