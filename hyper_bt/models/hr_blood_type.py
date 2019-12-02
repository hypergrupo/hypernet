# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class HrEmployeeBloodeType(models.Model):
    _inherit = 'hr.employee'

    # other fields
    blood_type = fields.Char(string='Tipo de Sangre', copy=False, domain=[(1, '=', 1)])
    allergies = fields.Char(string='Alergias', copy=False, index=False, domain=[(1, '=', 1)])
    reg_informativo = fields.Char(string='Reg. Infonavit', copy=False, index=False, domain=[(1, '=', 1)])
    reg_fonacot = fields.Char(string='Reg. Fonacot', copy=False, index=False, domain=[(1, '=', 1)])
    credito_fonacot = fields.Integer("Credito fonacot", copy=False, index=False)
    tarjeta_one_card = fields.Integer("Tarjeta one card", copy=False, index=False)

    @api.model
    def create(self, values):
        _logger.debug(values)
        return super(HrEmployeeBloodeType, self).create(values)