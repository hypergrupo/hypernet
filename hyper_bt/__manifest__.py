# -*- coding: utf-8 -*-
{
    'name': "Hyper_bloode_type",

    'summary': """
        Capa de personalización para las aplicaciones de Recursos Humanos en HyperSeguros tipo de sangre""",

    'description': """
        Long description of module's purpose
    """,

    'author': "David Pedraza",
    'website': "http://www.hyperseguros.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_bloode_type.xml',
    ]
}