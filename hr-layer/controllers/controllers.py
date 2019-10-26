# -*- coding: utf-8 -*-
from odoo import http

# class Hr-layer(http.Controller):
#     @http.route('/hr-layer/hr-layer/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr-layer/hr-layer/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr-layer.listing', {
#             'root': '/hr-layer/hr-layer',
#             'objects': http.request.env['hr-layer.hr-layer'].search([]),
#         })

#     @http.route('/hr-layer/hr-layer/objects/<model("hr-layer.hr-layer"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr-layer.object', {
#             'object': obj
#         })