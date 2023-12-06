from odoo import fields, models


class PlantillaSiro(models.Model):
    _name = "plantilla.siro"
    _order = "id desc"
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre")
    tipo = fields.Selection(selection=[('prepago_adt', 'Prepago (Adelantado)')], string="Tipo")
    dia_pago = fields.Integer(string="Día de Pago")
    crear_factura = fields.Integer(string="Crear Factura", help="Campo Dígito")
    tipo_impuesto = fields.Selection(selection=[('impuesto_inc', 'Impuesto Incluido')], string="Tipo Impuesto")
    dias_gracia = fields.Integer(string="Días de Gracia")
    aplicar_corte = fields.Selection(selection=[('2mesesV', '2 Meses vencidos')], string="Aplicar Corte")
    bajar_velocidad = fields.Boolean(default=False, string="Bajar Velocidad")
    primer_venc = fields.Integer()
    segundo_venc = fields.Integer()
    tercer_venc = fields.Integer()
