# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class HrContract(models.Model):
    _inherit = 'hr.contract'

    # other fields
    name = fields.Char(string='Referencia de Contrato', copy=False, index=False,required=True, default='Nuevo Contrato')

    # change
    @api.model
    def create(self, values):
        _logger.debug('Created')
        values['name'] = self.env['ir.sequence'].next_by_code('hr.contract.id')
        return super(HrContract, self).create(values)