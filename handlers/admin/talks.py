#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from . import admin, AdminHandler


class AdminTalksHandler(AdminHandler):
    @admin
    def get(self):
        pager = {}
        pager['qnty'] = min(max(int(self.get_argument('qnty', 10)), 1), 100)
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        talks = self.talks_ins.get_talks_list(pager['qnty'], (pager['page']-1)*pager['qnty'])
        if talks:
            pager['lgth'] = len(talks)

        self.render('admin/talks.html', pager=pager, talks=talks)


class AdminTalkHandler(AdminHandler):
    @admin
    def get(self):
        talk_id = self.get_argument('talk_id')
        talk = self.talks_ins.get_talk_by_id(talk_id)

        if not talk:
            self.flash(0, {'sta': 404})
            return

        self.render('admin/talk.html', talk=talk)

    @admin
    def post(self):
        try:
            talk_id = self.get_argument('talk_id')
            user_name = self.get_argument('user_name')
            user_mail = self.get_argument('user_mail')
            talk_rank = self.get_argument('talk_rank')
            talk_text = self.get_argument('talk_text')
            talk_utms = int(time.time())

            self.talks_ins.update_talk_by_id([user_name, user_mail, talk_rank, talk_text, talk_utms, talk_id])
            self.ualog(self.current_user, u'更新评论：' + str(talk_id))
            self.flash(1)
            return
        except:
            pass
        self.flash(0)


class AdminTalkDeleteHandler(AdminHandler):
    @admin
    def post(self):
        try:
            talk_id = self.get_argument('talk_id')
            talk_ctms = self.get_argument('talk_ctms')

            self.talks_ins.delete_talk_by_id(talk_id, talk_ctms)
            self.ualog(self.current_user, u'删除评论：' + str(talk_id))
            self.flash(1)
            return
        except:
            pass
        self.flash(0)
