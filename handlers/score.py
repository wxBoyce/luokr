#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler


class ScoreHandler(BaseHandler):
    def post(self):
        try:
            # update post scores
            self.flash(1)
        except:
            self.flash(0)
