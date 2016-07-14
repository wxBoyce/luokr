#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base


class Files(Base):

    def __init__(self):
        super(Files, self).__init__()

    def insert_user_logo_info(self, info_list):
        self.g_mysql.execute("insert into files(file_hash, file_base, file_path, file_type, file_memo, file_ctms) "
                             "values ('%s', '%s', '%s', '%s', '%s', '%s')" % tuple(info_list))
