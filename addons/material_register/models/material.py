# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name = 'material.register'
    _description = 'Material Register'

    code = fields.Char('Material Code', required=True)
    name = fields.Char('Material Name', required=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], 'Material Type', required=True)
    buy_price = fields.Float('Material Buy Price', required=True)
    produsen_id = fields.Many2one('produsen.register', 'Related Produsen', required=True)

    @api.constrains('code')
    def _check_unique_code(self):
        for record in self:
            if self.env['material.register'].search_count([('code', '=', record.code)]) > 1:
                raise ValidationError('Code material harus unik!')

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError('Harga Buy Price harus lebih dari 100.')
