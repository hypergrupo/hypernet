# -*- coding: utf-8 -*-
{
    'name': "HyperHR",

    'summary': """
        Capa de personalización para las aplicaciones de Recursos Humanos en HyperSeguros""",

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
    'depends': ['hr','hr_contract'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/hr_contract_sequence.xml',
        'data/hr_welcome_to_the_team_template.xml',
        'views/hr_employee.xml',
        'views/hr_contract.xml'
    ]
}