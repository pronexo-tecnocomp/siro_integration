from odoo import fields, models, api


class ResPartnerSiro(models.Model):
    _inherit = "res.partner"

    plantilla = fields.Many2one(comodel_name="plantilla.siro")

    tipo = fields.Selection(selection=[('prepago_adt', 'Prepago (Adelantado)')], string="Tipo")
    dia_pago = fields.Integer(string="Día de Pago")
    crear_factura = fields.Integer(string="Crear Factura")
    tipo_impuesto = fields.Selection(selection=[('impuesto_inc', 'Impuesto Incluido')], string="Tipo Impuesto")
    dias_gracia = fields.Integer(string="Días de Gracia")
    aplicar_corte = fields.Selection(selection=[('2mesesV', '2 Meses vencidos')], string="Aplicar Corte")
    bajar_velocidad = fields.Boolean(default=False, string="Bajar Velocidad")
    primer_venc = fields.Integer()
    segundo_venc = fields.Integer()
    tercer_venc = fields.Integer()
    @api.onchange('plantilla')
    def get_plantilla_data(self):
        for rec in self:
            if rec.plantilla:
                rec.tipo = rec.plantilla.tipo
                rec.dia_pago = rec.plantilla.dia_pago
                rec.crear_factura = rec.plantilla.crear_factura
                rec.tipo_impuesto = rec.plantilla.tipo_impuesto
                rec.dias_gracia = rec.plantilla.dias_gracia
                rec.aplicar_corte = rec.plantilla.aplicar_corte
                rec.bajar_velocidad = rec.plantilla.bajar_velocidad
                rec.primer_venc = rec.plantilla.primer_venc
                rec.segundo_venc = rec.plantilla.segundo_venc
                rec.tercer_venc = rec.plantilla.tercer_venc
            else:
                rec.tipo = False
                rec.dia_pago = False
                rec.crear_factura = False
                rec.tipo_impuesto = False
                rec.dias_gracia = False
                rec.aplicar_corte = False
                rec.bajar_velocidad = False
                rec.primer_venc = False
                rec.segundo_venc = False
                rec.tercer_venc = False