from odoo import fields, models
class TransaccionesSiro(models.Model):
    _name = "transacciones.siro"
    _order = "id desc"

    cliente = fields.Many2one(comodel_name="res.partner", string="Cliente")
    factura = fields.Many2one(comodel_name="account.move", string="Factura")
    legal = fields.Char(string="Legal")
    transaccion = fields.Char(string="Transacción")
    fecha_hora = fields.Datetime(string="Fecha & Hora")
    cobrado = fields.Float(string="Cobrado")
