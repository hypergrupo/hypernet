# -*- coding: utf-8 -*-

from botocore.exceptions import ClientError
import boto3
from odoo import models, fields, api

import logging