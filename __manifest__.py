# -*- coding: utf-8 -*-
{
    'name': "Gestión de Compras LCDA",

    'summary': """
        Módulo de Gestión de Compras Liceo de Cultura""",

    'description': """
        Módulo de gestión de compras, proveedores y productos de Liceo de Cultura y Difusión Artística de Talca
    """,

    'author': "Universidad de Talca",
    'website': "https://www.utalca.cl",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/view_producto.xml',
        'views/view_solicitudes.xml',
       # 'views/view_proveedor.xml'
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
