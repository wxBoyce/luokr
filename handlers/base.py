#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

import functools

import tornado.web
import tornado.escape


from models.users import Users
from utils.util import Utils
from utils.cache import Cache
from utils.tools import Tools

try:
    import urlparse  # py2
except ImportError:
    import urllib.parse as urlparse  # py3

try:
    from urllib import urlencode  # py2
except ImportError:
    from urllib.parse import urlencode  # py3


class BaseHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.users_ins = Users()

    # 重写get_current_user, 主要实现当前登陆用户获取
    def get_current_user(self):
        usid = self.get_cookie('_usid')
        auid = self.get_secure_cookie('_auid')
        auth = self.get_secure_cookie('_auth')
        if usid and auth:
            user = self.users_ins.get_user_by_id(usid)
            if user and user['user_auid'] == auid and Tools.generate_authword(user['user_atms'], user['user_salt']) == auth:
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

    def human_valid(self):                           # 验证码
        field = '_code'
        value = self.get_secure_cookie(field)
        if value:
            self.clear_cookie(field)
            str_input = self.get_argument(field, None)
            if str_input:
                value = tornado.escape.json_decode(value)
                return 'time' in value and 'code' in value \
                    and 0 < int(time.time()) - value['time'] < 60 \
                    and value['code'] == Utils.str_md5_hex(Utils.str_md5_hex(self.settings['cookie_secret']) + str_input + str(value['time']))
        return False

    def entry(self, sign, size=1, life=10, swap=False):   # 控制登陆尝试次数
        sign = 'entry@' + sign
        data = Cache.obtain(sign)
        if swap or not data:
            Cache.upsert(sign, size, life)
        return data

    def set_current_sess(self, user, days=30):
        self.set_cookie('_usid', str(user['user_id']), expires_days=days)
        self.set_secure_cookie('_auid', str(user['user_auid']), expires_days=days, httponly=True)
        self.set_secure_cookie('_auth', Tools.generate_authword(user['user_atms'], user['user_salt']))


def login(method):
    """Decorate methods with this to require that the user be logged in.

    If the user is not logged in, they will be redirected to the configured
    `login url <RequestHandler.get_login_url>`.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            if self.find_accept('json'):
                self.flash(0, {'sta': 403, 'url': self.get_login_url()})
                return

            if self.request.method in ("GET", "HEAD"):
                url = self.get_login_url()
                if "?" not in url:
                    if urlparse.urlsplit(url).scheme:
                        # if login url is absolute, make next absolute too
                        next_url = self.request.full_url()
                    else:
                        next_url = self.request.uri
                        if next_url.find('/index.py') == 0:
                            next_url = next_url.replace('/index.py', '', 1)

                    url += "?" + urlencode(dict(next=next_url))
                self.redirect(url)
                return
            self.flash(0, {'sta': 403})
            return
        return method(self, *args, **kwargs)
    return wrapper


def alive(method):
    @login
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if Tools.chk_user_is_live(self.current_user):
            return method(self, *args, **kwargs)
        else:
            self.flash(0, {'sta': 403, 'url': self.get_login_url()})
            return
    return wrapper
