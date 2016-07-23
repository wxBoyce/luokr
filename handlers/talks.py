#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler


class TalksHandler(BaseHandler):
    def get(self, _ext='.json'):
        pager = {}
        pager['qnty'] = min(max(int(self.get_argument('qnty', 10)), 1), 100)
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        talks = self.talks_ins.get_post_terms_by_post_id(self.get_argument('poid', ''),
                                                         self.get_runtime_conf('posts_talks_min_rank'), pager['qnty'],
                                                         (pager['page']-1)*pager['qnty'])
        if talks:
            pager['lgth'] = len(talks)

        self.flash(1, {'dat': {'talks': talks, 'pager': pager}}, _ext)
