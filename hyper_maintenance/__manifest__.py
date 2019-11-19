# -*- coding: utf-8 -*-
{
    'name': "HyperMaintenance",

    'summary': """
        Capa de personalización para las aplicaciones de Mantenimiento de Hyperseguros""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Pablo Adoue Peralta",
    'website': "http://www.hyperseguros.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['maintenance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/maintenance_request_sequence.xml',
        'data/maintenance_equipment_isabel_sequence.xml',
        'views/maintenance_request.xml'
    ]
}