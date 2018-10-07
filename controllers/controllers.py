# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class MySite(http.Controller):

    @http.route('/site/', auth='public')
    def index(self, **kw):
        return "Hello, from MySite"

    @http.route('/site/<name>/', auth='public')
    def dynamic_str(self, name):
        return '<h1>{}</h1>'.format(name)

    @http.route('/academy/<int:id>/', auth='public')
    def dynamic_num(self, id):
        return http.local_redirect('/web/login?redirect=/site/')
#        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    @http.route('/site/<name>/<int:id>/', auth='public')
    def dynamic_str_num(self, name, id):
        return '<h1>Name={} Num={} Type=({})</h1>'.format(name, id, type(id).__name__)

    @http.route('/my_site/my_site/', auth='public')
    def my_site(self, **kw):
        values = {'x': 'hello'}
        return request.render("my_site.test_template", values)

    # @http.route('/my_site/my_site/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('my_site.listing', {
    #         'root': '/my_site/my_site',
    #         'objects': http.request.env['my_site.my_site'].search([]),
    #     })
    #
    # @http.route('/my_site/my_site/objects/<model("my_site.my_site"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('my_site.object', {
    #         'object': obj
    #     })
