#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler


class TestHandler(BaseHandler):

    def get(self):
        self.write("Test")
