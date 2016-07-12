#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import tornado.escape


from models.users import Users


class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.users_ins = Users()

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

    def flash(self, isok, resp=None, _ext=''):      # 异常抛出处理
        if resp is None:
            resp = {}

        if isok:
            resp['err'] = 0
        else:
            resp['err'] = 1

        if 'sta' in resp and resp['sta']:
            self.set_status(resp['sta'])
        else:
            resp['sta'] = self.get_status()

        if 'msg' not in resp:
            resp['msg'] = self._reason
        if 'url' not in resp:
            resp['url'] = ''
        if 'dat' not in resp:
            resp['dat'] = {}

        if _ext == '.json' or self.find_accept('json'):
            self.write(tornado.escape.json_encode(resp))
        else:
            self.render('flash.html', resp=resp)

    def find_accept(self, name):
        return 'Accept' in self.request.headers and self.request.headers['Accept'].find(name) >= 0

    def human_valid(self):                           # 登陆态验证
        field = '_code'
        value = self.get_secure_cookie(field)
        if value:
            return True
        return False
