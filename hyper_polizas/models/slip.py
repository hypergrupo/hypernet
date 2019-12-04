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

    client=fields.Many2one('res.partner', string="Contratante", domain=[["is_client","=",True]])
    insured=fields.Many2one('res.partner', string="Asegurado Final", domain=[["is_client","=",True]])
    insurer=fields.Many2one('res.partner', string="Asegurado Final", domain=[["is_insurer","=",True]])
    agent=fields.Many2one('hr.employee', string="Agente", domain=[["job_rol","=","sales"]])
    insurance_line=fields.Selection(INSURANCE_LINE,string="Ramo")

    car_licence_plate=fields.Char(string="Placas")
    car_make=fields.Char(string="Marca")
    car_model=fields.Char(string="Modelo")
    car_vin=fields.Char(string="Número de Serie")
    car_year=fields.Integer(string="Año")
     
    premium=fields.Float(string="Prima")
    initial_premium=fields.Float(string="Prima Inicial")
    following_premium=fields.Float(string="Prima Subsecuente", compute="_following_premium", store=True)
     
    issue_date=fields.Date(string="Fecha de Emisión")
    in_force_date=fields.Date(string="Inicio de Vigencia")
    cancellation_date=fields.Date(string="Fecha de Cancelación")
    expiration_date=fields.Date(string="Fin de Vigencia")
    
    premium_modality = fields.Selection(PREMIUM_MODALITY, copy=False, index=0, domain=[(1, '=', 1)])
    payment_method= fields.Selection(PAYMENT_METHOD, copy=False, index=0, domain=[(1, '=', 1)])

    policy_number=fields.Char(string="Número de Póliza")


    # @api.model
    # def create(self, values):
    #     _logger.debug(values)
    #     initial_date = values['issue_date'] + datetime.timedelta(days = 30)
    #     for x in range(values['premium_modality']):
    #         if x == 0:
    #             super(self.env['x_billing_slip'].create({
    #                 'slip_id': values['id'],
    #                 'collection_employee': self.filtered('hr.employee') ,
    #                 'slip_collection': self.filtered('billing_slip'),
    #                 'amount_receivable': values['initial_premium'],
    #                 'start_of_payment': self.issue_date,
    #                 'payment_limit': initial_date,
    #             }))
    #         else:
    #             super(self.env['x_billing_slip'].create({
    #                 'slip_id': values['id'],
    #                 'collection_employee': self.filtered('hr.employee') ,
    #                 'slip_collection': self.filtered('x_billing_slip'),
    #                 'amount_receivable': values['following_premium'],
    #                 'start_of_payment': initial_date + datetime.timedelta(days = 1),
    #                 'payment_limit': initial_date + datetime.timedelta(days = 30),
    #             }))
    #             initial_date = initial_date + datetime.timedelta(days = 30)
        


@api.depends('premium','initial_premium','premium_modality')
def _following_premium(self):
    for record in self:
        premium_modality=int(record.premium_modality)
        if premium_modality==1:
            record.initial_premium=record.premium
            record.following_premium=0
        elif premium_modality >1:
            record.following_premium=(record.premium-record.initial_premium)/(premium_modality-1)

