{
    'name': 'Digizilla',
    'version': '1.0',
    'description': 'digizilla module',
    'author': 'Omar Swailam',
    # 'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'views/digizilla_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'digizilla/static/src/js/form_view_customization.js'],
    },
    'application': True,
}
