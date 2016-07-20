#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import admin, AdminHandler


class AdminConfsHandler(AdminHandler):
    @admin
    def get(self):
        pager = {}
        pager['qnty'] = min(max(int(self.get_argument('qnty', 10)), 1), 100)
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        confs = self.confs_ins.get_confs(pager['qnty'], (pager['page']-1)*pager['qnty'])

        if confs:
            pager['lgth'] = len(confs)

        self.render('admin/confs.html', pager=pager, confs=confs)


class AdminConfHandler(AdminHandler):
    @admin
    def get(self):
        conf_name = self.get_argument('conf_name')
        conf = self.confs_ins.get_conf_by_name(conf_name)
        if not conf:
            self.flash(0, {'sta': 404})
            return

        self.render('admin/conf.html', entry=conf)

    @admin
    def post(self):
        try:
            conf_name = self.get_argument('conf_name')
            conf_vals = self.get_argument('conf_vals')

            self.confs_ins.insert_conf(conf_name, conf_vals)

            self.flash(1, {'msg': '更新配置成功'})
        except:
            self.flash(0)


class AdminConfCreateHandler(AdminHandler):
    @admin
    def get(self):
        self.render('admin/conf-create.html')

    @admin
    def post(self):
        try:
            conf_name = self.get_argument('conf_name')
            conf_vals = self.get_argument('conf_vals')

            if len(conf_name) > 32:
                self.flash(0, {'msg': '配置键长度不能超过32个字符'})
                return
            if self.confs_ins.is_exists(conf_name):
                self.flash(0, {'msg': '配置键已存在'})
                return

            self.confs_ins.insert_conf(conf_name, conf_vals)
            self.ualog(self.current_user, u"新增配置：" + conf_name, conf_vals)
            self.flash(1, {'msg': '新增配置成功'})
        except:
            self.flash(0)


class AdminConfDeleteHandler(AdminHandler):
    @admin
    def post(self):

        try:
            conf_name = self.get_argument('conf_name')
            conf_vals = self.get_runtime_conf(conf_name)
            self.confs_ins.delete(conf_name)
            self.ualog(self.current_user, u"删除配置：" + conf_name, conf_vals)
            self.flash(1, {'msg': '删除配置成功'})
        except:
            self.flash(0)

