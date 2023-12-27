from odoo import fields, models


class PlantillaSiro(models.Model):
    _name = "plantilla.siro"
    _order = "id desc"
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre")
    tipo = fields.Selection(selection=[('post_pago', 'Postpago (Vencido)'), ('prepago_adt', 'Prepago (Adelantado)')], string="Tipo")
    dia_pago = fields.Selection([
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28')],
        string="Día de Pago")

    crear_factura = fields.Selection([
        ('desactivado', 'Desactivado'),
        ('1dia', '1 Día antes'),
        ('2dias', '2 Días antes'),
        ('3dias', '3 Días antes'),
        ('4dias', '4 Días antes'),
        ('5dias', '5 Días antes'),
        ('6dias', '6 Días antes'),
        ('7dias', '7 Días antes'),
        ('8dias', '8 Días antes'),
        ('9dias', '9 Días antes'),
        ('10dias', '10 Días antes'),
        ('11dias', '11 Días antes'),
        ('12dias', '12 Días antes'),
        ('13dias', '13 Días antes'),
        ('14dias', '14 Días antes'),
        ('15dias', '15 Días antes'),
        ('16dias', '16 Días antes'),
        ('17dias', '17 Días antes'),
        ('18dias', '18 Días antes'),
        ('19dias', '19 Días antes'),
        ('20dias', '20 Días antes'),
        ('21dias', '21 Días antes'),
        ('22dias', '22 Días antes'),
        ('23dias', '23 Días antes'),
        ('24dias', '24 Días antes'),
        ('25dias', '25 Días antes')],
        string="Crear Factura")

    tipo_impuesto = fields.Selection(
        selection=[('ninguno', 'Ninguno'), ('mas_impuestos', 'Mas Impuestos'), ('impuesto_inc', 'Impuesto Incluido')],
        string="Tipo Impuesto")
    dias_gracia = fields.Selection([
        ('0', '0 Días'),
        ('1', '1 Día'),
        ('2', '2 Días'),
        ('3', '3 Días'),
        ('4', '4 Días'),
        ('5', '5 Días'),
        ('6', '6 Días'),
        ('7', '7 Días'),
        ('8', '8 Días'),
        ('9', '9 Días'),
        ('10', '10 Días'),
        ('11', '11 Días'),
        ('12', '12 Días'),
        ('13', '13 Días'),
        ('14', '14 Días'),
        ('15', '15 Días'),
        ('16', '16 Días'),
        ('17', '17 Días'),
        ('18', '18 Días'),
        ('19', '19 Días'),
        ('20', '20 Días'),
        ('21', '21 Días'),
        ('22', '22 Días'),
        ('23', '23 Días'),
        ('24', '24 Días'),
        ('25', '25 Días')],
        string="Días de Gracia")

    aplicar_corte = fields.Selection([
        ('desactivado', 'Desactivado'),
        ('1mesV', '1 Mes vencido'),
        ('2mesesV', '2 Meses vencidos'),
        ('3mesesV', '3 Meses vencidos'),
        ('4mesesV', '4 Meses vencidos'),
        ('5mesesV', '5 Meses vencidos'),
        ('6mesesV', '6 Meses vencidos'),
        ('7mesesV', '7 Meses vencidos'),
        ('8mesesV', '8 Meses vencidos'),
        ('9mesesV', '9 Meses vencidos'),
        ('10mesesV', '10 Meses vencidos'),
        ('11mesesV', '11 Meses vencidos'),
        ('12mesesV', '12 Meses vencidos')],
        string="Aplicar Corte", default='desactivado')
    bajar_velocidad = fields.Boolean(default=False, string="Bajar Velocidad")
    primer_venc = fields.Integer()
    segundo_venc = fields.Integer()
    tercer_venc = fields.Integer()
