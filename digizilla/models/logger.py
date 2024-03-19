from odoo import models, fields


class Logger(models.Model):
    _name = 'logger'
    _description = 'Logger Model'

    record_id = fields.Integer(string='Record ID', required=True)
    field_name = fields.Char(string='Field Name', required=True)
    old_value = fields.Char(string='Old Value')
    new_value = fields.Char(string='New Value')
