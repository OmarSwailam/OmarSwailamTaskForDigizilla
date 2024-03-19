from odoo import models, fields

class Tag(models.Model):
    _name = 'tag'
    _description = 'Custom tag'

    name = fields.Char(string='Tag Name', required=True)
