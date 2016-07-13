#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


class Utils(object):

    @staticmethod
    def str_md5_hex(val):
        return hashlib.md5(val).hexdigest()
