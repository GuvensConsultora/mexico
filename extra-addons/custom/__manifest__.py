# -*- coding: utf-8 -*-
{
    'name': "Custom",

    'summary': "Prueba inicial del modulo",

    'description': """
Este es el primer modulo luego de reconstruir este esquema
    """,

    'author': "Guvens",
    'website': "https://www.guvens.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Ventas',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

