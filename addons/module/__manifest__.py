{
    'name': 'module',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Leon',
    'category': 'Services',
    'description': 'Create Odoo Module for test task',
    'data': [
        'security/ir.model.access.csv',
        'views/my_first_model_views.xml',
    ],
    'installable': True,
    'application': True,
}
