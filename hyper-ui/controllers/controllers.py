# -*- coding: utf-8 -*-
from odoo import http

# class Hyper-ui(http.Controller):
#     @http.route('/hyper-ui/hyper-ui/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hyper-ui/hyper-ui/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hyper-ui.listing', {
#             'root': '/hyper-ui/hyper-ui',
#             'objects': http.request.env['hyper-ui.hyper-ui'].search([]),
#         })

#     @http.route('/hyper-ui/hyper-ui/objects/<model("hyper-ui.hyper-ui"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hyper-ui.object', {
#             'object': obj
#         })