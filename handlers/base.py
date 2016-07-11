#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.escape


class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    # 重写get_current_user, 主要实现当前登陆用户获取
    def get_current_user(self):
        user = {
            'user_name': "admin"
        }
        return user

    # 获取当前运行时段的配置
    def get_runtime_conf(self, name):
        ret = ""
        return ret

    def jsons(self, json):
        if json is None or json == '':
            return None
        return tornado.escape.json_decode(json)
