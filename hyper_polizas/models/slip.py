# -*- coding: utf-8 -*-

 from odoo import models, fields, api


class slip(models.Model):
     _name = 'slip'
     _description = 'Module for creating'

     cancellation_date=fields.Date(string="Fecha de Cancelación")
     car_licence_plate=fields.Char(string="Placas")
     car_make=fields.Char(string="Marca")
     car_model=fields.Char(string="Modelo")
     car_vin=fields.Char(string="Número de Serie")
     car_year=fields.Integer(string="Año")
     expiration_date=fields.Date(string="Fin de Vigencia")



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
