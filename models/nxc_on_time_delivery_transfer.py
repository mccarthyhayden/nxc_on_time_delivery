from odoo import api, fields, models

class NxcOnTimeDeliveryTransfer(models.Model):
    _inherit = 'stock.picking'
    
    #On-Time Delivery Field
    completed_on_time = fields.Boolean(string="Completed On Time", compute="_compute_on_time", readonly=True)

    # Calculate the value of the on-time delivery field".
    @api.onchange('date_deadline', 'date_done')
    def _compute_on_time(self):
        for record in self:
          if ((record.date_deadline != False and record.date_done != False) and (record.date_done < record.date_deadline)):
            record['completed_on_time'] = True
          else:
            record['completed_on_time'] = False