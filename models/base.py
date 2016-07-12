#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dbmanage import g_mysql


class Base(object):

    def __init__(self):
        super(Base, self).__init__()
        self.g_mysql = g_mysql
