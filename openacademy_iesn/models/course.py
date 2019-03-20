# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api, exceptions, _


class Course(models.Model):
    _inherit = 'openacademy.course'

    # add here link to tasks and a integer to store the amount of credits
