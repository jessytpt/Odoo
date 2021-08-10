# -*- coding: utf-8 -*-
from odoo import http

# class Jessenia(http.Controller):
#     @http.route('/jessenia/jessenia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jessenia/jessenia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jessenia.listing', {
#             'root': '/jessenia/jessenia',
#             'objects': http.request.env['jessenia.jessenia'].search([]),
#         })

#     @http.route('/jessenia/jessenia/objects/<model("jessenia.jessenia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jessenia.object', {
#             'object': obj
#         })