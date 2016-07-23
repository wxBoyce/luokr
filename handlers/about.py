#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler


class AboutHandler(BaseHandler):
    def get(self):
        self.render('about.html')
