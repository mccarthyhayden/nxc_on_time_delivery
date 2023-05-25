{
    'name': 'NXC On Time Delivery Addon',
    'version': '15.0',
    'category': 'inventory',
    'summary': 'Adds a "Completed On Time" field to transfers of "outgoing" type. This field is computed from deadline and transfer date.',
    'description': 'This custom module was developed for Next Chapter Manufacturing to enable tracking of on-time deliveries.',
    'author': 'Hayden McCarthy',
    'website': 'https://www.nxcmfg.com',
    'depends': ['stock'],
    'data': [
        'views/view_nxc_on_time_delivery_transfer_form.xml',
    ],
    'installable': True,
    'auto_install': False,
}

