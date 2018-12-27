# -*- coding: utf-8 -*-
#  Copyright (C) 2004-2018 CodeFish (<http://www.codefish.com.eg>).
#  Copyright 2018 CodeFish
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class MrpProductionDepartments(models.Model):
    _name = 'hr.department'
    _inherit = 'hr.department'

    mrp_department = fields.Boolean('Production Department')


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    mrp_department = fields.Many2one('hr.department', string="Production Department")


class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    mrp_department = fields.Many2one('hr.department', string="Production Department",
                                     related='product_id.mrp_department')
