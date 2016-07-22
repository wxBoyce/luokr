#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from . import admin, AdminHandler


class AdminLinksHandler(AdminHandler):
    @admin
    def get(self):
        pager = {}
        pager['qnty'] = min(max(int(self.get_argument('qnty', 10)), 1), 100)
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        links = self.links_ins.get_links_list(pager['qnty'], (pager['page']-1)*pager['qnty'])

        if links:
            pager['lgth'] = len(links)

        self.render('admin/links.html', pager=pager, links=links)


class AdminLinkHandler(AdminHandler):
    @admin
    def get(self):
        link_id = self.get_argument('link_id')
        link = self.links_ins.get_link_by_id(link_id)

        if not link:
            self.flash(0, {'sta': 404})
            return

        self.render('admin/link.html', entry=link)

    @admin
    def post(self):
        try:
            link_id = self.get_argument('link_id')
            link_name = self.get_argument('link_name')
            link_href = self.get_argument('link_href')
            link_desp = self.get_argument('link_desp')
            link_rank = self.get_argument('link_rank')
            link_utms = int(time.time())

            self.links_ins.update_link_by_info([link_name, link_href, link_desp, link_rank,
                                                link_utms, link_id])

            self.ualog(self.current_user, u'更新链接：' + str(link_id))
            self.flash(1)
            return
        except:
            pass
        self.flash(0)


class AdminLinkCreateHandler(AdminHandler):
    @admin
    def get(self):
        self.render('admin/link-create.html')

    @admin
    def post(self):
        try:
            link_name = self.get_argument('link_name')
            link_href = self.get_argument('link_href')
            link_desp = self.get_argument('link_desp')
            link_rank = self.get_argument('link_rank')
            link_utms = int(time.time())
            link_ctms = link_utms

            self.links_ins.insert_link_info([link_name, link_href, link_desp, link_rank, link_ctms, link_utms])
            self.ualog(self.current_user, u"新增链接", link_href)
            self.flash(1)
            return
        except:
            pass
        self.flash(0)


class AdminLinkDeleteHandler(AdminHandler):
    @admin
    def post(self):
        try:
            link_id = self.get_argument('link_id')
            link_utms = self.get_argument('link_utms')
            self.links_ins.delete_link_by_id(link_id, link_utms)
            self.ualog(self.current_user, u'删除链接：' + str(link_id))
            self.flash(1)
            return
        except:
            pass
        self.flash(0)
