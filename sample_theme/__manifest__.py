# __manifest__.py
{
    'name': 'Sample Theme',
    'description': 'A minimal sample theme with a single page',
    'version': '1.0',
    'author': 'Odoo Valencia',
    'license': 'LGPL-3',
    'depends': ['website','web'],
    'data': [
        'views/layout.xml',
        'views/page.xml',
    ],
    'installable': True,
    'application': False,
}
