#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import hashlib


class Utils(object):

    @staticmethod
    def str_md5_hex(val):
        return hashlib.md5(val).hexdigest()

    @staticmethod
    def build_links(val, opt=' target="_blank"'):
        exp = re.compile(
            r'('
            r'(?:http|ftp)s?://'  # http:// or https://
            r'[a-z0-9-]+(?:\.[a-z0-9-]+)*'  # domain or ip...
            r'(?::\d+)?'  # optional port
            r'(?:/[^"\'<>\s]*)?'  # optional segs
            r')', re.IGNORECASE)
        return exp.sub(r'<a href="\1"' + opt + r'>\1</a>', val)
