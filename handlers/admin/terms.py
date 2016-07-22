#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import admin, AdminHandler


class AdminTermsHandler(AdminHandler):
    @admin
    def get(self):
        pager = {}
        pager['qnty'] = min(max(int(self.get_argument('qnty', 10)), 1), 100)
        pager['page'] = max(int(self.get_argument('page', 1)), 1)
        pager['lgth'] = 0

        terms = self.terms_ins.get_terms_list(pager['qnty'], (pager['page']-1)*pager['qnty'])

        if terms:
            pager['lgth'] = len(terms)

        self.render('admin/terms.html', terms=terms, pager=pager)


class AdminTermHandler(AdminHandler):
    @admin
    def get(self):
        term_id = self.get_argument('term_id')
        term = self.terms_ins.get_term_by_id(term_id)
        if not term:
            self.flash(0, {'sta': 404})
            return

        self.render('admin/term.html', entry=term)

    @admin
    def post(self):
        try:
            term_id = self.get_argument('term_id')
            term_name = self.get_argument('term_name')
            self.terms_ins.update_term_name_by_id(term_name, term_id)
        except:
            pass
        self.flash(0)


class AdminTermCreateHandler(AdminHandler):
    @admin
    def get(self):
        self.render('admin/term-create.html')
