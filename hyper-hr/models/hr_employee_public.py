# -*- coding: utf-8 -*-

from botocore.exceptions import ClientError
import boto3
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


EMPLOYEE_STATUS_SELECTION = [
    ('new', 'Nuevo'), ('hired', 'Contratado'), ('fired', 'Baja')]


class HrEmployeePublic(models.Model):
    _inherit = "hr.employee"

    no_rfc = fields.Char(string='RFC')