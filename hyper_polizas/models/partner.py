# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    is_client = fields.Boolean(string='Es Cliente', copy=True, index=False, domain=[(1, '=', 1)])
    is_insurer = fields.Boolean(string='Es Aseguradora', copy=True, index=False, domain=[(1, '=', 1)])
    
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
