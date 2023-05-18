from . import models
from . import views
from odoo import api, SUPERUSER_ID

def _setup(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.model.data'].sudo().create({
        'name': 'view_nxc_on_time_delivery_transfer_form',
        'module': 'nxc_on_time_delivery',
        'res_id': env.ref('nxc_on_time_delivery.view_nxc_on_time_delivery_transfer_form').id,
        'model': 'ir.ui.view',
    })

def uninstall_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.model.data'].sudo().search([
        ('module', '=', 'nxc_on_time_delivery'),
        ('name', '=', 'view_nxc_on_time_delivery_transfer_form')
    ]).unlink()

def post_init_hook(cr, registry):
    _setup(cr, registry)