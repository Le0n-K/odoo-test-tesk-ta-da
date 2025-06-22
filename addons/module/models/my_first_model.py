from odoo import models, fields

class MyFirstModel(models.Model):
    _name = 'my.first.model'
    _description = 'My First Model'

    name = fields.Char(string='Name')
    places = fields.Integer(string='Places')
    active = fields.Boolean(string='Active', default=True)
