# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    # other fields
    name = fields.Char(string='Petición de mantenimiento', copy=False, index=False,required=True, default='Nuevo')

    # change
    @api.model
    def create(self, values):
        values['name'] = self.env['ir.sequence'].next_by_code('maintenance.request.id')
        return super(MaintenanceRequest, self).create(values)