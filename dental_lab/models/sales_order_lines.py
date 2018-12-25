# -*- coding: utf-8 -*-
#  Copyright (C) 2004-2018 CodeFish (<http://www.codefish.com.eg>).
#  Copyright 2018 CodeFish
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    # Upper Left Fields
    ul1 = fields.Boolean('1')
    ul2 = fields.Boolean('2')
    ul3 = fields.Boolean('3')
    ul4 = fields.Boolean('4')
    ul5 = fields.Boolean('5')
    ul6 = fields.Boolean('6')
    ul7 = fields.Boolean('7')
    ul8 = fields.Boolean('8')
    # Upper Right Fields
    ur1 = fields.Boolean('1')
    ur2 = fields.Boolean('2')
    ur3 = fields.Boolean('3')
    ur4 = fields.Boolean('4')
    ur5 = fields.Boolean('5')
    ur6 = fields.Boolean('6')
    ur7 = fields.Boolean('7')
    ur8 = fields.Boolean('8')
    # Lower Left Fields
    ll1 = fields.Boolean('1')
    ll2 = fields.Boolean('2')
    ll3 = fields.Boolean('3')
    ll4 = fields.Boolean('4')
    ll5 = fields.Boolean('5')
    ll6 = fields.Boolean('6')
    ll7 = fields.Boolean('7')
    ll8 = fields.Boolean('8')
    # Lower Right Fields
    lr1 = fields.Boolean('1')
    lr2 = fields.Boolean('2')
    lr3 = fields.Boolean('3')
    lr4 = fields.Boolean('4')
    lr5 = fields.Boolean('5')
    lr6 = fields.Boolean('6')
    lr7 = fields.Boolean('7')
    lr8 = fields.Boolean('8')

    #All
    allt = fields.Boolean('case')

    # Colors Model Fields
    color = fields.Many2one('colors', string='Color', required=True)

    # Modify Base Fields
    product_uom_qty = fields.Integer(compute='_value_pc', string='Quantity')

    # Api to sum tooth boolean checkboxes values
    @api.multi
    @api.depends(
        'ul1', 'ul2', 'ul3', 'ul4', 'ul5', 'ul6', 'ul7', 'ul8', 'ur1', 'ur2', 'ur3', 'ur4', 'ur5', 'ur6', 'ur7', 'ur8', 'll1', 'll2', 'll3', 'll4', 'll5', 'll6', 'll7', 'll8', 'lr1', 'lr2', 'lr3', 'lr4', 'lr5', 'lr6', 'lr7', 'lr8', 'allt'
    )
    def _value_pc(self):
        for line in self:
            if line.allt == 1:
                line.product_uom_qty = 1
            else:
                line.product_uom_qty = line.ul1 + line.ul2 + line.ul3 + line.ul4 + line.ul5 + line.ul6 + line.ul7 + line.ul8 + line.ur1 + line.ur2 + line.ur3 + line.ur4 + line.ur5 + line.ur6 + line.ur7 + line.ur8 + line.ll1 + line.ll2 + line.ll3 + line.ll4 + line.ll5 + line.ll6 + line.ll7 + line.ll8 + line.lr1 + line.lr2 + line.lr3 + line.lr4 + line.lr5 + line.lr6 + line.lr7 + line.lr8