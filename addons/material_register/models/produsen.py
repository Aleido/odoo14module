from odoo import api, fields, models

class Produsen(models.Model):
    _name = 'produsen.register'
    _description = 'Produsen Register'

    name = fields.Char('Produsen Name', required=True)
    contact = fields.Char('Produsen Contact Number')
    address = fields.Char('Produsen Address')
