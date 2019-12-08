# -*- coding: utf-8 -*-

from odoo import models, fields, api

STATUS = [
    ('schedule', 'Programado'), ('billing', 'Cobranza'), ('payed', 'Pagado'), ('cancelled', 'Cancelado')]


class BillingSlip(models.Model):
    _name = 'billing_slip'
    _description = 'Billing Slip Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(default="Nuevo")
    slip = fields.Many2one('slip', ondelete='cascade', index=True)
    status = fields.Selection(STATUS, default="schedule")
    responsible=fields.Many2one('hr.employee', string="Responsable", domain=[["job_role","=",'billing']])

    premium = fields.Float(string="Prima")
    due_premium = fields.Float(string="Prima por pagar")
    payed_premium = fields.Float(string="Prima pagada", default=0)

    start_date = fields.Date(string="Fecha")
    due_date = fields.Date(string="Fecha límite")
    payment_date = fields.Date(string="Fecha de Pago")

    # Related Fields
    client = fields.Many2one(string="Contratante", related='slip.client')
    insurer = fields.Many2one(string="Aseguradora", related='slip.insurer')
    policy_number = fields.Char(
        string="Número de Póliza", related='slip.policy_number')

    @api.model
    def create(self, values):
        values['name'] = self.env['ir.sequence'].next_by_code(
            'sequence.billing_slip.id')

        return super(BillingSlip, self).create(values)

    def write(self, values):
        if 'premium' in values.keys():
            premium = values['premium']
        else:
            premium = self.premium

        if 'payed_premium' in values.keys():
            values['due_premium'] = premium-values['payed_premium']
            if (premium-values['payed_premium']) == 0:
                values['status']='payed'

        return super(BillingSlip, self).write(values)