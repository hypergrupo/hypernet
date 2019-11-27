# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    # other fields
    name = fields.Char(string='Petición de mantenimiento',
                       copy=False, index=False, required=True, default='Nuevo')

    # change
    @api.model
    def create(self, values):
        if 'name' in values.keys():
            values['name'] = self.env['ir.sequence'].next_by_code(
                'account.analytic_account.id')+"-"+values['name']
            return super(AccountAnalyticAccount, self).create(values)
