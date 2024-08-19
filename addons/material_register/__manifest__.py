# -*- coding: utf-8 -*-
{
    'name': "Material Register",

    'summary': """
        """,

    'description': """
        Ini adalah tool Odoo module untuk melakukan listing material secara sederhana
    """,

    'author': "Ridho",
    'website': "",
    'category': 'Custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
        'views/produsen_views.xml',
        'views/menu.xml',
        'data/data_produsen.xml',
        'data/data_material.xml',
    ],
}
