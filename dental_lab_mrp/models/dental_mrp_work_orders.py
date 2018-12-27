# -*- coding: utf-8 -*-
#  Copyright (C) 2004-2018 CodeFish (<http://www.codefish.com.eg>).
#  Copyright 2018 CodeFish
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MrpWorkOrders(models.Model):
    _inherit = 'mrp.workorder'

    sale_order_id = fields.Many2one('sale.order', string="Sale Order", related='production_id.sale_order_id',
                                    store=True, translate=True)
    sale_order_line_id = fields.Many2one('sale.order.line', string="Sale Order Line",
                                         related='production_id.sale_order_line_id',
                                         store=True, translate=True)
    color = fields.Many2one('colors', related='production_id.color', string="Color")
    allt = fields.Selection('case', related='production_id.allt')
    user_id = fields.Many2one('res.users', string="Responsible", related='production_id.user_id')
    partner_id = fields.Many2one('res.partner', string="Customer", related='production_id.partner_id')
    patient_name = fields.Char('Patient Name', related='production_id.patient_name', store=True)

    # Upper Left Fields
    ul1 = fields.Boolean('1', related='production_id.ul1')
    ul2 = fields.Boolean('2', related='production_id.ul2')
    ul3 = fields.Boolean('3', related='production_id.ul3')
    ul4 = fields.Boolean('4', related='production_id.ul4')
    ul5 = fields.Boolean('5', related='production_id.ul5')
    ul6 = fields.Boolean('6', related='production_id.ul6')
    ul7 = fields.Boolean('7', related='production_id.ul7')
    ul8 = fields.Boolean('8', related='production_id.ul8')
    # Upper Right Fields
    ur1 = fields.Boolean('1', related='production_id.ur1')
    ur2 = fields.Boolean('2', related='production_id.ur2')
    ur3 = fields.Boolean('3', related='production_id.ur3')
    ur4 = fields.Boolean('4', related='production_id.ur4')
    ur5 = fields.Boolean('5', related='production_id.ur5')
    ur6 = fields.Boolean('6', related='production_id.ur6')
    ur7 = fields.Boolean('7', related='production_id.ur7')
    ur8 = fields.Boolean('8', related='production_id.ur8')
    # Lower Left Fields
    ll1 = fields.Boolean('1', related='production_id.ll1')
    ll2 = fields.Boolean('2', related='production_id.ll2')
    ll3 = fields.Boolean('3', related='production_id.ll3')
    ll4 = fields.Boolean('4', related='production_id.ll4')
    ll5 = fields.Boolean('5', related='production_id.ll5')
    ll6 = fields.Boolean('6', related='production_id.ll6')
    ll7 = fields.Boolean('7', related='production_id.ll7')
    ll8 = fields.Boolean('8', related='production_id.ll8')
    # Lower Right Fields
    lr1 = fields.Boolean('1', related='production_id.lr1')
    lr2 = fields.Boolean('2', related='production_id.lr2')
    lr3 = fields.Boolean('3', related='production_id.lr3')
    lr4 = fields.Boolean('4', related='production_id.lr4')
    lr5 = fields.Boolean('5', related='production_id.lr5')
    lr6 = fields.Boolean('6', related='production_id.lr6')
    lr7 = fields.Boolean('7', related='production_id.lr7')
    lr8 = fields.Boolean('8', related='production_id.lr8')