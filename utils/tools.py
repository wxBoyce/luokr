#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import random
import hashlib


class Tools(object):

    @staticmethod
    def generate_password(pswd, salt):
        return hashlib.md5('AL.pswd:' + hashlib.md5(str(pswd) + '#' + str(salt)).hexdigest()).hexdigest()

    @staticmethod
    def generate_authword(atms, salt):
        return hashlib.md5('AL.auth:' + hashlib.md5(str(atms) + '$' + str(salt)).hexdigest()).hexdigest()

    @staticmethod
    def chk_user_if_perm(user, perm):
        try:
            user = dict(user)
            return user and 'user_perm' in user and user['user_perm'] & perm == perm
        except:
            return False

    @staticmethod
    def chk_user_is_live(user):
        return Tools.chk_user_if_perm(user, 0x00000001)
