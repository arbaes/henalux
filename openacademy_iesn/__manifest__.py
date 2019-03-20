# -*- coding: utf-8 -*-
{
    'name': "IESN - Odoo",

    'summary': """
        Course management, now with GIFS""",

    'author': "Odoo",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Academy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['openacademy', 'project'],

    # always loaded
    'data': [
        'views/project.xml',
        #'views/sessions.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
