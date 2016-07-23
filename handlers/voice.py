#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from utils.tools import Tools
from base import BaseHandler


class VoiceHandler(BaseHandler):
    def post(self):
        if not self.human_valid():
            self.flash(0, {'msg': '验证码错误'})
            return

        post = self.posts_ins.get_post_by_id(self.get_argument('poid'))
        if not post:
            self.flash(0, {'msg': '文章不存在'})
            return

        rank = '0'
        usid = '0'
        if self.get_argument('auth', False) and self.current_user:
            if Tools.chk_user_is_live(self.current_user):
                rank = self.get_runtime_conf('posts_talks_min_rank')
            usid = self.current_user['user_id']
            name = self.current_user['user_name']
            mail = self.current_user['user_mail']
        else:
            name = self.get_argument('name')
            mail = self.get_argument('mail')

        text = self.get_argument('text')
        s_time = int(time.time())

        try:
            # insert info to talks
            # update posts_refc
            self.talks_ins.insert_info_to_talks([post['post_id'], self.request.remote_ip, usid, name, mail, text, rank, s_time, s_time])
        except:
            self.flash(0)