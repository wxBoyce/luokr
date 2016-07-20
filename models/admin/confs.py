#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from models.base import Base


class Confs(Base):
    def __init__(self):
        super(Confs, self).__init__()
        self._cache = {}
        self.reload()

    def reload(self, datum=None):
        if datum is not None:
            ret = self.g_mysql.query('select conf_name, conf_vals from confs')
            if ret:
                for row in ret:
                    self._cache[row['conf_name']] = row['conf_vals']

    def get_confs(self, limit, offset):
        return self.g_mysql.query("select * from confs order by conf_ctms desc limit %s offset %s", limit, offset)

    def get_conf_by_name(self, conf_name):
        return self.g_mysql.get("select * from confs where conf_name = %s", conf_name)

    def insert_conf(self, name, vals):
        self.g_mysql.execute("replace into confs(conf_name, conf_vals, conf_ctms) values('%s', '%s', %s)" % (name, vals, int(time.time())))

    def is_exists(self, name):
        ret = self.g_mysql.get("select 1 from confs where conf_name = %s", name)
        return bool(ret)

    def obtain_conf_by_name(self, name):
        if name not in self._cache:
            ret = self.g_mysql.get('select conf_vals from confs where conf_name=%s' % name)
            if ret:
                self._cache[name] = ret['conf_vals']
            else:
                self._cache[name] = None
        return self._cache[name]

    def delete(self, name):
        self.g_mysql.execute("delete from confs where conf_name='%s'" % name)
        self._cache[name] = None
