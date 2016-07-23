#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

from utils.mailx import Mailx

from base import BaseHandler


class EmailHandler(BaseHandler):
    def post(self):
        if not self.human_valid():
            self.flash(0, {'msg': '验证码错误'})
        name = self.get_argument('name')
        mail = self.get_argument('mail')
        text = self.get_argument('text')
        s_time = int(time.time())

        self.email_ins.insert_email_into([self.request.remote_ip, name, mail, text, s_time, s_time])
        self.flash(1)
        self.send_email('%s <%s>' % (name, mail), self.jsons(self.get_runtime_conf('mails')),
                        'Received Feedback (%s)' % time.strftime('%F %T %Z', time.localtime(s_time)),
                        'Mail From %s <%s>:\r\n\r\n%s' % (name, mail, text))

    def send_email(self, *args, **kwargs):
        conf = self.jsons(self.get_runtime_conf('mailx'))
        if conf and 'smtp_able' in conf and conf['smtp_able']:
            threading.Thread(target=Mailx(conf).send, args=args, kwargs=kwargs).start()
