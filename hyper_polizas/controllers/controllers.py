# -*- coding: utf-8 -*-
# from odoo import http


# class HyperPolizas(http.Controller):
#     @http.route('/hyper_polizas/hyper_polizas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hyper_polizas/hyper_polizas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hyper_polizas.listing', {
#             'root': '/hyper_polizas/hyper_polizas',
#             'objects': http.request.env['hyper_polizas.hyper_polizas'].search([]),
#         })

#     @http.route('/hyper_polizas/hyper_polizas/objects/<model("hyper_polizas.hyper_polizas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hyper_polizas.object', {
#             'object': obj
#         })
