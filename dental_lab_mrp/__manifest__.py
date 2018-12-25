# -*- coding: utf-8 -*-
{
    'name': "Dental Lab MRP",

    'summary': """
        Simpal Module for Dental Lab
        """,

    'description': """
       Simpal Module for Dental Lab
    """,

    'author': "CodeFish",
    'website': "https://www.codefish.com.eg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': "Manufacturing",
    'version': '10.0.2',

    # any module necessary for this one to work correctly
    'depends': ['mrp',
                'sale',
                'dental_lab',
                'hr',
                'product'
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/mrp_production_view.xml',
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