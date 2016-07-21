#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import hashlib
import mimetypes

from . import admin, AdminHandler


class AdminFilesHandler(AdminHandler):
    @admin
    def get(self):
        pager = {}
        pager['qnty'] = min(max(int(self.get_argument('qnty', 10)), 1), 100)
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        files = self.files_ins.get_files_list(pager['qnty'], (pager['page']-1)*pager['qnty'])
        if files:
            pager['lgth'] = len(files)

        self.render('admin/files.html', pager=pager, files=files)


class AdminFileHandler(AdminHandler):
    @admin
    def get(self):
        self.flash(0)


class AdminFileUploadHandler(AdminHandler):

    def check_xsrf_cookie(self):
        return True

    @admin
    def get(self):
        self.render('admin/file-upload.html')

    @admin
    def post(self):
        if 'upload' not in self.request.files or len(self.request.files['upload']) < 1:
            self.flash(0, {'msg': '没有上传文件'})
            return

        res = self.request.files['upload'][0]

        if 'content_type' not in res or res['content_type'].find('/') < 1 or len(res['content_type']) > 128:
            self.flash(0, {'msg': '文件类型错误'})
            return

        if 'filename' not in res or res['filename'] == '':
            self.flash(0, {'msg': '文件名称错误'})
            return

        ets = mimetypes.guess_all_extensions(res['content_type'])
        ext = os.path.splitext(res['filename'])[1].lower()
        if ets and ext not in ets:
            ext = ets[0]

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

        if self.get_argument('CKEditorFuncNum', None) is not None:
            out = '<script type="text/javascript">'
            out += 'window.parent.CKEDITOR.tools.callFunction(%s,"%s","%s");' % (self.get_argument('CKEditorFuncNum'), url, '')
            out += '</script>'
            self.write(out)
        else:
            self.flash(1, {'msg': "上传成功", 'ext': {'url': url}})


class AdminFileDeleteHandler(AdminHandler):
    @admin
    def post(self):
        try:
            fid = self.get_argument('file_id')
            ctm = self.get_argument('file_ctms')

            res = self.files_ins.get_file_by_id(fid)

            if not res:
                self.flash(0)
                return

            uri = self.settings['root_path'] + res['file_base'] + res['file_path']
            if os.path.isfile(uri):
                os.remove(uri)
                dir = os.path.dirname(uri)
                while dir != self.settings['root_path'] and os.path.isdir(dir) and not os.listdir(dir):
                    os.rmdir(dir)
                    dir = os.path.dirname(dir)

            self.files_ins.delete_file_by_id(fid, ctm)
        except:
            pass
        self.flash(0)