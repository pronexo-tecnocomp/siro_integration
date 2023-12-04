from odoo import fields, models


class PlantillaSiro(models.Model):
    _name = "plantilla.siro"
    _order = "id desc"
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre")
    tipo = fields.Selection(selection=[('prepago_adt', 'Prepago (Adelantado)')], string="Tipo")
    dia_pago = fields.Selection(selection=[('15', '15')], string="Día Pago")
    crear_factura = fields.Selection(selection=[('13a', '13 Días antes')], string="Crear Factura")
    tipo_impuesto = fields.Selection(selection=[('impuesto_inc', 'Impuesto Incluido')], string="Tipo Impuesto")
    dias_gracia = fields.Selection(selection=[('3dia', '3 Días')], string="Días de Gracia")
    aplicar_corte = fields.Selection(selection=[('2mesesV', '2 Meses vencidos')], string="Aplicar Corte")
    bajar_velocidad = fields.Selection(selection=[('desactivado', 'Desactivado')], string="Bajar Velocidad")
    primer_venc = fields.Integer()
    segundo_venc = fields.Integer()
    tercer_venc = fields.Integer()