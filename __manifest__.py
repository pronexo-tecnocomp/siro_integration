# -*- coding: utf-8 -*-
{

    'name': 'Siro',
    'version': '1',
    'summary': 'Siro Integration',
    'sequence': -101,
    'description': """Integracion con siro de banco roela""",
    'author': 'DEVMAN',
    'maintainer': 'DEVMAN',
    'license': 'AGPL-3',

    'depends': ['base','contacts','account'],

    'data': [
        'views/siro_account_move.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
