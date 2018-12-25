# -*- coding: utf-8 -*-
#  Copyright (C) 2004-2018 CodeFish (<http://www.codefish.com.eg>).
#  Copyright 2018 CodeFish
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    sale_order_id = fields.Many2one('sale.order', string="Sale Order", compute="_compute_sale_order",
                                    store=True, translate=True)
    sale_order_line_id = fields.Many2one('sale.order.line', string="Sale Order Line", compute="_compute_sale_order",
                                         store=True, translate=True)
    color = fields.Many2one('colors', related='sale_order_line_id.color', string="Color")
    allt = fields.Boolean('case', related='sale_order_line_id.allt')
    mrp_department = fields.Many2one('hr.department', string="Production Department",
                                     related='sale_order_line_id.mrp_department')
    user_id = fields.Many2one('res.users', string="Responsible", related='sale_order_line_id.production_employee')
    partner_id = fields.Many2one('res.partner', string="Customer", related='sale_order_id.partner_id')
    patient_name = fields.Char('Patient Name', related='sale_order_id.patient_name', store=True)

    # Upper Left Fields
    ul1 = fields.Boolean('1', related='sale_order_line_id.ul1')
    ul2 = fields.Boolean('2', related='sale_order_line_id.ul2')
    ul3 = fields.Boolean('3', related='sale_order_line_id.ul3')
    ul4 = fields.Boolean('4', related='sale_order_line_id.ul4')
    ul5 = fields.Boolean('5', related='sale_order_line_id.ul5')
    ul6 = fields.Boolean('6', related='sale_order_line_id.ul6')
    ul7 = fields.Boolean('7', related='sale_order_line_id.ul7')
    ul8 = fields.Boolean('8', related='sale_order_line_id.ul8')
    # Upper Right Fields
    ur1 = fields.Boolean('1', related='sale_order_line_id.ur1')
    ur2 = fields.Boolean('2', related='sale_order_line_id.ur2')
    ur3 = fields.Boolean('3', related='sale_order_line_id.ur3')
    ur4 = fields.Boolean('4', related='sale_order_line_id.ur4')
    ur5 = fields.Boolean('5', related='sale_order_line_id.ur5')
    ur6 = fields.Boolean('6', related='sale_order_line_id.ur6')
    ur7 = fields.Boolean('7', related='sale_order_line_id.ur7')
    ur8 = fields.Boolean('8', related='sale_order_line_id.ur8')
    # Lower Left Fields
    ll1 = fields.Boolean('1', related='sale_order_line_id.ll1')
    ll2 = fields.Boolean('2', related='sale_order_line_id.ll2')
    ll3 = fields.Boolean('3', related='sale_order_line_id.ll3')
    ll4 = fields.Boolean('4', related='sale_order_line_id.ll4')
    ll5 = fields.Boolean('5', related='sale_order_line_id.ll5')
    ll6 = fields.Boolean('6', related='sale_order_line_id.ll6')
    ll7 = fields.Boolean('7', related='sale_order_line_id.ll7')
    ll8 = fields.Boolean('8', related='sale_order_line_id.ll8')
    # Lower Right Fields
    lr1 = fields.Boolean('1', related='sale_order_line_id.lr1')
    lr2 = fields.Boolean('2', related='sale_order_line_id.lr2')
    lr3 = fields.Boolean('3', related='sale_order_line_id.lr3')
    lr4 = fields.Boolean('4', related='sale_order_line_id.lr4')
    lr5 = fields.Boolean('5', related='sale_order_line_id.lr5')
    lr6 = fields.Boolean('6', related='sale_order_line_id.lr6')
    lr7 = fields.Boolean('7', related='sale_order_line_id.lr7')
    lr8 = fields.Boolean('8', related='sale_order_line_id.lr8')

    @api.multi
    @api.depends('procurement_ids')
    def _compute_sale_order(self):
        mto_route = self.env.ref('stock.route_warehouse0_mto')
        for production in self:
            if mto_route.id in production.product_id.route_ids.ids:
                for prod_procurement in production.procurement_ids:
                    if prod_procurement.move_dest_id:
                        procurement = prod_procurement.move_dest_id.procurement_id
                        if procurement.sale_line_id:
                            production.sale_order_id = procurement.sale_line_id.order_id
                            production.sale_order_line_id = procurement.sale_line_id.id


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    production_id = fields.One2many('mrp.production', 'sale_order_id', 'Manufacturing Orders')