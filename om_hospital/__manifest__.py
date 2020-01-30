{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Hospital Management',
    'description': 'Module for Managing the hospital',
    'category': 'Extra Tools',
    'author': 'AdesDev',
    'sequence': '0',
    'website': 'https://digitalfarmer.github.io',
    'license': 'AGPL-3',
    'depends': ['base','mail','sale'],
    'data':[
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/appointment_view.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
        'data/sequence.xml',
    ],
    'demo':[],
    'installable': True,
    'auto_install': False,

}