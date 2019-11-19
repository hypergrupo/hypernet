# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    # other fields
    name = fields.Char(string='Equipo', copy=False, index=False,required=True, default='Nuevo')

    # change
    @api.model
    def create(self, values):
        if 'category_id' in values.keys():
            categories = self.env["maintenance.equipment.category"].search([("id","=",values['category_id'])])
            category=categories[0]
            if(category['name'])=='Extensión PBX (Isabel)':
                values['name'] = self.env['ir.sequence'].next_by_code('maintenance.equipment.isabel.id')
        return super(MaintenanceEquipment, self).create(values)