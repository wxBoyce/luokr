#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import shell, ShellHandler


class ShellPanelHandler(ShellHandler):

    @shell
    def get(self):
        self.render('shell/panel.html', user=self.current_user)
