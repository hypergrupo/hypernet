# -*- coding: utf-8 -*-

from odoo import models, fields, api

PREMIUM_MODALITY = [
    ('12', 'Monthly'), ('4', 'Trimestral'), ('2', 'Semestral'), ('1', 'Anual')]
PAYMENT_METHOD = [
    ('credit', 'Tarjeta de Crédito'), ('debit', 'Tarjeta de Débito'), ('pos', 'Punto de Venta')]
INSURANCE_LINE = [
    ('car', 'Auto')]

class slip(models.Model):
    _name = 'slip'
    _description = 'Module for creating'

    client=fields.Many2One('res.partner', string="Contratante", domain=[["is_client","=",True]])
    insured=fields.Many2One('res.partner', string="Asegurado Final", domain=[["is_client","=",True]])
    insurer=fields.Many2One('res.partner', string="Asegurado Final", domain=[["is_insurer","=",True]])
    insurance_line=fields.Selection(INSURANCE_LINE,string="Ramo")

    car_licence_plate=fields.Char(string="Placas")
    car_make=fields.Char(string="Marca")
    car_model=fields.Char(string="Modelo")
    car_vin=fields.Char(string="Número de Serie")
    car_year=fields.Integer(string="Año")
     
    premium=fields.Float(string="Prima")
    initial_premium=fields.Float(string="Prima Inicial")
    following_premium=fields.Float(string="Fin de Vigencia")
     
    issue_date=fields.Date(string="Fecha de Emisión")
    in_force_date=fields.Date(string="Inicio de Vigencia")
    cancellation_date=fields.Date(string="Fecha de Cancelación")
    expiration_date=fields.Date(string="Fin de Vigencia")
    
    premium_modality = fields.Selection(PREMIUM_MODALITY, copy=False, index=0, domain=[(1, '=', 1)])
    payment_method= fields.Selection(PAYMENT_METHOD, copy=False, index=0, domain=[(1, '=', 1)])

    policy_number=fields.Char(string="Número de Póliza")



#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
