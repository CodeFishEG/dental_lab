# -*- coding: utf-8 -*-
from odoo import http

# class DentalLab(http.Controller):
#     @http.route('/dental_lab/dental_lab/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dental_lab/dental_lab/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dental_lab.listing', {
#             'root': '/dental_lab/dental_lab',
#             'objects': http.request.env['dental_lab.dental_lab'].search([]),
#         })

#     @http.route('/dental_lab/dental_lab/objects/<model("dental_lab.dental_lab"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dental_lab.object', {
#             'object': obj
#         })