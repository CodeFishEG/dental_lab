# -*- coding: utf-8 -*-
#  Copyright (C) 2004-2018 CodeFish (<http://www.codefish.com.eg>).
#  Copyright 2018 CodeFish
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, api, _

class CrmLead(models.Model):
    _name = 'crm.lead'
    _inherit = 'crm.lead'

    CASE_TYPE = [
        ('normal', 'Normal'),
        ('full', 'Full Case'),
        ('half', 'Half a Case')
    ]

    CASE_STATUS = [
        ('new', 'New'),
        ('rest', 'Restoration'),
        ('rep', 'Repair')
    ]

    patient_name = fields.Char('Patient Name')
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
    allt = fields.Selection(CASE_TYPE, string='Case Type')

    # Colors Model Fields
    d_color = fields.Many2one('colors', string='Color')

    # Case Statues
    case_statues = fields.Selection(CASE_STATUS, string='Case Statues')

    product_id = fields.Many2one('product.product', string='Product')
    antagonist = fields.Char(string='Antagonist')
    bite = fields.Char(string='Bite')




