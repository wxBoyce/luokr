#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import hashlib
import mimetypes

from . import shell, ShellHandler

from utils.tools import Tools


class ShellPanelHandler(ShellHandler):

    @shell
    def get(self):

        self.render('shell/panel.html', user=self.current_user)

    @shell
    def post(self, *args):
        try:
            user = self.current_user
            if self.entry('panel:user#' + str(user['user_id'])):
                self.flash(0, {'msg': '操作太频繁,请稍后再试', 'sta': 429})
                return

            user_mail = self.get_argument('mail')
            user_sign = self.get_argument('sign', '')
            user_meta = self.get_argument('meta', '')
            user_pswd = self.get_argument('pswd', None)
            user_npwd = self.get_argument('npwd', None)
            user_rpwd = self.get_argument('rpwd', None)

            if not user_mail:
                self.flash(0)
                return

            if not Tools.chk_is_user_mail(user_mail):
                self.flash(0, {'msg': '无效的用户邮箱'})
                return

            if user_mail != user['user_mail'] and self.users_ins.get_user_by_mail(user_mail):
                self.flash(0, {'msg': '用户邮箱已存在'})
                return

            user_logo = user['user_logo']
            if 'logo' in self.request.files and len(self.request.files['logo']) > 0:
                res = self.request.files['logo'][0]

                if 'filename' not in res or res['filename'] == '':
                    self.flash(0, {'msg': '无效的文件名称'})
                    return

                if 'body' not in res or not (0 < len(res['body']) < 1024 * 1024):
                    self.flash(0, {'msg': '无效的文件长度'})
                    return

                if 'content_type' not in res or res['content_type'].find('/') < 1 or len(res['content_type']) > 128:
                    self.flash(0, {'msg': '无效的文件类型'})
                    return

                ets = mimetypes.guess_all_extensions(res['content_type'])
                ext = os.path.splitext(res['filename'])[1].lower()
                if ets and ext not in ets:
                    ext = ets[0]

                ets = [".jpg", ".jpeg", ".gif", ".png", ".bmp"]
                if ext not in ets:
                    self.flash(0, {'msg': '文件类型不支持'})
                    return

                md5 = hashlib.md5()
                md5.update(res['body'])
                key = md5.hexdigest()

                dir = '/www'
                url = '/upload/' + time.strftime('%Y/%m/%d/') + key[0] + key[1] + key[30] + key[
                    31] + '/' + key + ext
                uri = self.settings['root_path'] + dir + url
                url = '/static/img/www' + url

                if not os.path.exists(os.path.dirname(uri)):
                    os.makedirs(os.path.dirname(uri), mode=0777)

                fin = open(uri, 'w')
                fin.write(res['body'])
                fin.close()

                # 对应信息存入数据库
                self.files_ins.insert_user_logo_info([key, dir, url, res['content_type'], res['filename'], int(time.time())])
                user_logo = url

            if user_npwd:
                if not len(user_npwd) >= 6 or user_npwd != user_rpwd or Tools.generate_password(user_pswd, user['user_salt']) != user['user_pswd']:
                    self.flash(0, {'msg': '密码输入错误'})
                    return

                user_auid = Tools.generate_randauid()
                user_salt = Tools.generate_randsalt()
                self.users_ins.update_user_info_by_pwd([user_auid, user_mail, user_logo, user_sign, user_meta,
                                                        Tools.generate_password(user_npwd, user_salt), user_salt,
                                                        int(time.time()), int(time.time()), user['user_id']])
            else:
                self.users_ins.update_user_info_by_other([user_mail, user_logo, user_sign, user_meta,
                                                          int(time.time()), user['user_id']])

            self.flash(1, {'msg': '更新成功'})
            return
        except:
            pass

        self.flash(0)
