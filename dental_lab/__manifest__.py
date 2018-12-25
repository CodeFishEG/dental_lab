# -*- coding: utf-8 -*-
{
    'name': "Dental Lab",

    'summary': """
        Simpal Module for Dental Lab
        """,

    'description': """
       Simpal Module for Dental Lab
    """,

    'author': "CodeFish",
    'website': "http://www.codefish.com.eg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '10.0.2',

    # any module necessary for this one to work correctly
    'depends': ['sale',
                'hr',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/colors.xml',
        'views/sale_order_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "images": [
        'static/description/banner.png'
    ],
    'price': 10.00,
    'currency': 'EUR',
}