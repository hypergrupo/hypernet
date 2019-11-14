# -*- coding: utf-8 -*-

from botocore.exceptions import ClientError
import boto3
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


EMPLOYEE_STATUS_SELECTION = [
    ('new', 'Nuevo'), ('hired', 'Contratado'), ('fired', 'Baja')]


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    # File Fields
    file_birth_certificate = fields.Binary('Acta de Nacimiento')
    file_address_certificate = fields.Binary('Comprobante de Domicilio')
    file_curp = fields.Binary('Certificado CURP')
    file_social_security = fields.Binary('Inscripción NSS')
    file_job_description = fields.Binary('Descripción de Puesto')
    file_bank_statement = fields.Binary('Estado de Cuenta')
    file_school_certificate = fields.Binary('Comprobante de Estudios')
    file_id = fields.Binary('Identificación')
    file_tax_id = fields.Binary('Cédula Fiscal')
    file_kardex = fields.Binary('Kardex')

    # other fields
    no_rfc = fields.Char(string='RFC', copy=False,
                         index=False, domain=[(1, '=', 1)])
    curp = fields.Char(string='CURP', copy=False,
                       index=False, domain=[(1, '=', 1)])
    nss = fields.Char(string='NSS', copy=False,
                      index=False, domain=[(1, '=', 1)])
    status = fields.Selection(EMPLOYEE_STATUS_SELECTION, copy=False, index=1, domain=[
                              (1, '=', 1)], default='new')

    # change
    @api.model
    def create(self, values):
        _logger.debug('Created')
        return super(HrEmployee, self).create(values)

    def write(self, values):
        _logger.debug('Updated')
        return super(HrEmployee, self).write(values)
