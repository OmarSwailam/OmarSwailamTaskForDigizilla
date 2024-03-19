from odoo import models, fields


class Digizilla(models.Model):
    _name = 'digizilla'
    _description = 'Digizilla model'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender',
                              tracking=True)
    country = fields.Many2one('res.country', string='Country')
    joining_date = fields.Date(string='Joining Date', default=fields.Date.today)
    tags = fields.Many2many('tag', string='Tags')
    customers = fields.Many2many('res.partner', string='Customers')
    company_id = fields.Many2one('res.company', string='Company', required=True)
    notes = fields.Text(string='Notes')
    comments = fields.Char(string='Comments')

    logger_ids = fields.One2many('logger', 'record_id', string='Logger')

    def write(self, vals):
        old_vals = self.read()[0].items()
        old_vals = {key: val for key, val in old_vals if key in vals}
        logger_data = {
            **{key: {"old_val": old_vals[key], "new_val": new_val} for key, new_val in vals.items()}
        }
        self._create_logger(self.id, logger_data)
        res = super(Digizilla, self).write(vals)
        return res

    def _create_logger(self, record_id, logger_data):
        for field in logger_data:
            logger_obj = self.env["logger"].create({
                "record_id": record_id,
                "field_name": field,
                "old_value": logger_data[field]["old_val"],
                "new_value": logger_data[field]["new_val"]
            })
