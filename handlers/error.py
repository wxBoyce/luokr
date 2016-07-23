#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers.base import BaseHandler


class ErrorHandler(BaseHandler):
    def get(self):
        self.send_error(404)

    def post(self):
        self.send_error(404)
