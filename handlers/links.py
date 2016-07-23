#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler


class LinksHandler(BaseHandler):
    def get(self):
        links = self.links_ins.get_links()

        self.render('links.html', links=links)
