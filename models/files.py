#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base


class Files(Base):

    def __init__(self):
        super(Files, self).__init__()

    def insert_user_logo_info(self, info_list):
        self.g_mysql.execute("insert into files(file_hash, file_base, file_path, file_type, file_memo, file_ctms) "
                             "values ('%s', '%s', '%s', '%s', '%s', '%s')" % tuple(info_list))

    def get_files_list(self, limit, offset):
        return self.g_mysql.query("select * from files order by file_id desc limit %s offset %s", limit, offset)

    def get_file_by_id(self, fid):
        return self.g_mysql.get('select * from filess where file_id=%s', fid)

    def delete_file_by_id(self, fid, ctm):
        self.g_mysql.execute("delete from files where file_id=%s and file_ctms=%s", fid, ctm)