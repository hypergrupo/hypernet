# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime

import logging
_logger = logging.getLogger(__name__)

PREMIUM_MODALITY = [
    ('12', 'Monthly'), ('4', 'Trimestral'), ('2', 'Semestral'), ('1', 'Anual')]
PAYMENT_METHOD = [
    ('credit', 'Tarjeta de Crédito'), ('debit', 'Tarjeta de Débito'), ('pos', 'Punto de Venta')]
INSURANCE_LINE = [
    ('car', 'Auto')]

STATUS = [
    ('quote', 'Cotizado'),('issued', 'Emitido'),('in_force', 'Vigente'),('expired', 'Expirado'),('cancelled', 'Cancelado')]

class Slip(models.Model):
    _name = 'slip'
    _description = 'Insurance Slip Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(default="Nuevo")

    billing_slip= fields.One2many('billing_slip','slip')

    client=fields.Many2one('res.partner', string="Contratante", domain=[["is_client","=",True]])
    insured=fields.Many2one('res.partner', string="Asegurado Final", domain=[["is_client","=",True]])
    insurer=fields.Many2one('res.partner', string="Aseguradora", domain=[["is_insurer","=",True]])
    agent=fields.Many2one('res.partner', string="Agente", domain=[["job_role","=","sales"]])
    insurance_line=fields.Selection(INSURANCE_LINE,string="Ramo")

    status=fields.Selection(STATUS, default="quote")

    car_licence_plate=fields.Char(string="Placas")
    car_make=fields.Char(string="Marca")
    car_model=fields.Char(string="Modelo")
    car_vin=fields.Char(string="Número de Serie")
    car_year=fields.Integer(string="Año")
     
    premium=fields.Float(string="Prima")
    initial_premium=fields.Float(string="Prima Inicial")
    following_premium=fields.Float(string="Prima Subsecuente")
     
    issue_date=fields.Date(string="Fecha de Emisión")
    in_force_date=fields.Date(string="Inicio de Vigencia")
    cancellation_date=fields.Date(string="Fecha de Cancelación")
    expiration_date=fields.Date(string="Fin de Vigencia")
    
    premium_modality = fields.Selection(PREMIUM_MODALITY, copy=False, index=0, domain=[(1, '=', 1)], default="1")
    payment_method= fields.Selection(PAYMENT_METHOD, copy=False, index=0, domain=[(1, '=', 1)])

    policy_number=fields.Char(string="Número de Póliza")

    @api.onchange('issue_date','in_force_date')
    def _in_force_date(self):
        if self.issue_date != False and not self.in_force_date:
            self.in_force_date=self.issue_date
            self.expiration_date=self.issue_date + datetime.timedelta(days = 366)
        elif self.in_force_date != False and not self.issue_date:
            self.issue_date=self.in_force_date
            self.expiration_date=self.expiration_date + datetime.timedelta(days = 366)

        if self.in_force_date!= False:
            self.expiration_date=self.in_force_date + datetime.timedelta(days = 366)
    
    @api.onchange('premium','initial_premium','premium_modality')
    def _premium_change(self):
        modality=int(self.premium_modality)

        premium=float(self.premium)
        initial_premium=float(self.initial_premium)        

        if modality==1:
            self.initial_premium=self.premium
            modality=2
        
        self.following_premium=(premium-initial_premium)/(modality-1)
    
    @api.model
    def create(self, values):
        #Cast the required values 
        premium=float(values['premium'])
        initial_premium=float(values['initial_premium'])        
        modality=int(values['premium_modality'])

        in_force_date=datetime.datetime.strptime(values['in_force_date'], '%Y-%m-%d')

        following_premium=(premium-initial_premium)/(modality-1)


        values['name'] = self.env['ir.sequence'].next_by_code('sequence.slip.id')

        #Create the slip
        slip=super(Slip, self).create(values)
        
        #Itterate to create the number of needed payments
        for x in range(modality):
            start_date=in_force_date+datetime.timedelta(x*365/12)
            due_date=start_date + datetime.timedelta(days = 30)
            if x==0:
                due_premium=initial_premium
            else:
                due_premium=following_premium

            billing_slip = self.env['billing_slip']
            billing_slip.create({
                'name': '',
                'slip': slip.id,
                'premium': due_premium,
                'due_premium': due_premium,
                'start_date': start_date,
                'due_date': due_date
            })

        return slip
                    


    #@api.onchange('issue_date','in_force_date')
    #def _expiration_date(self):
    #    if not self.in_force_date:
    #        self.in_force_date=self.issue_date            

    #    if self.issue_date != self.in_force_date:
    #        expiration_date=self.in_force_date+datetime.timedelta(days = 366)
    #    else:
    #        expiration_date=self.expiration_date+datetime.timedelta(days = 366)

        #self.in_force_date=self.issue_date
    #    self.expiration_date = expiration_date


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
