
from odoo import fields, models


class ExtendsResCompany(models.Model):
	_name = 'res.company'
	_inherit = 'res.company'

	siro_id = fields.Many2one('siro.config', 'Siro')

