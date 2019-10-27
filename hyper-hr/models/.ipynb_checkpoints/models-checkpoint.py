# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

import boto3
#AWS S3 client used to upload the picture of the employees when created
s3 = boto3.resource('s3')


EMPLOYEE_STATUS_SELECTION=[('new','Nuevo'),('hired','Contratado'),('fired','Baja')]

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    #File Fields
    file_birth_certificate=fields.Binary("Acta de Nacimiento")
    file_address_certificate=fields.Binary("Comprobante de Domicilio")
    file_curp=fields.Binary("Certificado CURP")
    file_social_security=fields.Binary("Inscripción NSS")
    file_job_description=fields.Binary("Descripción de Puesto")
    file_bank_statement=fields.Binary("Estado de Cuenta")
    file_school_certificate=fields.Binary("Comprobante de Estudios")
    file_id=fields.Binary("Identificación")
    file_tax_id=fields.Binary("Cédula Fiscal")

    #other fields
    tax_id=fields.Char("RFC")
    curp=fields.Char("CURP")
    nss=fields.Char("NSS")
    status=fields.Selection(EMPLOYEE_STATUS_SELECTION,default='new')

    @api.model
    def create(self, values):
        _logger.debug("Created")
        return super().create(values)

    def write(self, values):
        #_logger.debug(len(self.image_1920))
        if 'image_1920' in values:
            #Data to upload to S3
            data = values.image_1920
            #key to use
            key=self.id+".png"
            #Upload to s3
            s3.Bucket('hypernet-storage').put_object(Key='test.jpg', Body=data)
            
            _logger.debug("Se ha actualizado la foto")
        return super().write(values)
    
#    @api.multi
#    def write(self, vals):
#        return super(ResPartner, self).write(values)




# class hr-layer(models.Model):
#     _name = 'hr-layer.hr-layer'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100