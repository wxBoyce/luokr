#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import tornado.escape

from base import BaseHandler

from utils.util import Utils
from utils.captcha.image import gen_randoms, gen_captcha


class CheckHandler(BaseHandler):

    def get(self, _ext='.jpeg'):
        text = gen_randoms().strip()
        int_time = int(time.time())

        self.set_secure_cookie('_code', tornado.escape.json_encode(dict(code=Utils.str_md5_hex(
            Utils.str_md5_hex(self.settings['cookie_secret']) + text.lower() + str(int_time)), time=int_time)),
                               expires_days=None)

        self.set_header('Cache-Control', 'no-cache')
        self.add_header('Cache-Control', 'no-store')

        self.set_header('Content-Type', 'image/jpeg')
        self.write(gen_captcha(text, 'jpeg'))
