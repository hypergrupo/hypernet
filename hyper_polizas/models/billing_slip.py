# -*- coding: utf-8 -*-

from odoo import models, fields, api

STATUS = [
    ('12', 'Monthly'), ('4', 'Trimestral'), ('2', 'Semestral'), ('1', 'Anual')]


class billing_slip(models.Model):
    _name = 'slip'
    _description = 'Module for creating'

    id_resposable = fields.Many2one('hr.employee', string='Responsable', domain=[["job_rol","=","billing"]])
    slip_id = fields.Many2one('slip.id', string='Id de slip')
    amount_receivable = fields.Float(string='Monto a cobrar')
    amount_paid = fields.Float(string='Monto pagado')
    star_of_payment = fields.Date(string='Inicio de pago')
    payment_limit = fields.Date(string='Limite de pago')
    status = fields.Selection(STATUS, copy=False, index=0, domain=[1, '=', 1])
