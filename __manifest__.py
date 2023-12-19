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

    'depends': ['base', 'contacts', 'account'],

    'data': [
        'data/cron.xml',
        'data/sequence.xml',
        'report/report.xml',
        'report/boleta_pago.xml',
        'security/ir.model.access.csv',
        'views/siro_config.xml',
        'views/siro_account_move.xml',
        'views/res_company_customization.xml',
        'views/res_partner_plantilla.xml',
        'views/res_partner_custom_view.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
