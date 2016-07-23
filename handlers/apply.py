#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler


class ApplyHandler(BaseHandler):
    def get(self):
        self.redirect("/about#email")
