# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


EMPLOYEE_STATUS_SELECTION = [
    ('new', 'Nuevo'), ('hired', 'Contratado'), ('training', 'Capacitación'), ('active', 'Liberado'),('fired', 'Baja')]


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
    no_rfc = fields.Char(string='RFC', copy=False, index=False, domain=[(1, '=', 1)])
    curp = fields.Char(string='CURP', copy=False, index=False, domain=[(1, '=', 1)])
    nss = fields.Char(string='NSS', copy=False, index=False, domain=[(1, '=', 1)])
    status = fields.Selection(EMPLOYEE_STATUS_SELECTION, copy=False, index=1, domain=[(1, '=', 1)], default='new')
    job_functions = fields.Html(string="Responsabilidades", copy=False, index=False)
    welcome_email=fields.Boolean(string='Correo de Bienvenida', default=False)
    farewell_email=fields.Boolean(string='Correo de Despedida', default=False)


    # change
    @api.model
    def create(self, values):
        _logger.debug('Created')
        return super(HrEmployee, self).create(values)

    def write(self, values):
        _logger.debug(values)
        if 'status' in values.keys():
            if values['status']=='active' and self.welcome_email==False:
                template = self.env.ref('hyper_hr.email_template_welcome_to_the_team')
                self.env['mail.template'].browse(template.id).send_mail(self.id)
                values['welcome_email'] = True

        return super(HrEmployee, self).write(values)
    
premium_modality=int(record.x_premium_modality)

if premium_modality>1:
    following_premium=(record.x_premium-record.x_initial_premium)/(premium_modality-1)
elif premium_modality==1:
    following_premium=(record.x_premium-record.x_initial_premium)

record.write({
    'x_following_premium'=following_premium
})

