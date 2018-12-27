# -*- coding: utf-8 -*-
#  Copyright (C) 2004-2018 CodeFish (<http://www.codefish.com.eg>).
#  Copyright 2018 CodeFish
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _
from odoo.tools.translate import _

class Colors(models.Model):
    _name = 'colors'

    # Colors Fields
    name = fields.Char('Color Name')