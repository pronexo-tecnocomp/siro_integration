import datetime
import math

from odoo import fields, models, api
from odoo.exceptions import ValidationError

RELLENO = "0000000000000000000000000000000"
SECUENCIA_VERIFICADORA = [
    1, 3, 5, 7, 9, 3, 5, 7, 9, 3,
    5, 7, 9, 3, 5, 7, 9, 3, 5, 7,
    9, 3, 5, 7, 9, 3, 5, 7, 9, 3,
    5, 7, 9, 3, 5, 7, 9, 3, 5, 7,
    9, 3, 5, 7, 9, 3, 5, 7, 9, 3,
    5, 7, 9, 3
]
DIGITO_VERIFICADOR_ADICIONAL = 5


class SiroCodeBar(models.Model):
    _inherit = "account.move"

    empresa_servicio = fields.Char(default="0447", readonly=True, size=4)
    identificador_concepto = fields.Char(size=1)
    identificador_cuenta = fields.Char(size=10)
    identificador_usuario = fields.Integer(size=8)

    fecha_1er_vto = fields.Date(size=6)
    importe_1er_vto = fields.Float(digits=(7, 2))

    dias_2do_vto = fields.Integer(size=2)
    importe_2do_vto = fields.Float(digits=(7, 2))

    dias_3do_vto = fields.Integer(size=2)
    importe_3er_vto = fields.Float(digits=(7, 2))

    codigo_barra = fields.Char()
    codigo_pago_elect = fields.Char(string="Código Pago Electronico")

    def check_identificador_cuenta(self, rec):
        if rec.id:
            if rec.identificador_cuenta.__len__() != 10:
                raise ValidationError("El número de identificador de cuenta debe tener una cantidad de 10 caracteres.")

    def armaFecha(self, fecha):
        if fecha:
            dd = datetime.date.strftime(fecha, "%d").zfill(2)
            mm = datetime.date.strftime(fecha, "%m").zfill(2)
            yy = datetime.date.strftime(fecha, "%Y")[2:]

            fecha = yy + mm + dd
        return fecha

    def armaImporte(self, importe):
        if importe > 0:
            return str(importe).replace(".", "").zfill(7)
        else:
            return str(importe).replace(".", "").zfill(7)

    # FUNCION QUE EJECUTA EL CRON
    def generar_codigo_barra(self):
        code_config = self.env['siro.config'].search([], order='id desc', limit=1)
        invoices = self.env['account.move'].search([])
        if code_config.company_id.siro_id:
            for rec in invoices:
                self.check_identificador_cuenta(code_config)
                primer_digito_verificador = 0
                segundo_digito_verificador = 0
                try:
                    fecha_1er_vto = self.armaFecha(rec.fecha_1er_vto)
                    importe_1er_vto = self.armaImporte(rec.importe_1er_vto)
                    importe_2do_vto = self.armaImporte(rec.importe_2do_vto)
                    importe_3er_vto = self.armaImporte(rec.importe_3er_vto)

                    if rec:
                        codigo_barras = code_config.empresa_servicio
                        codigo_barras += code_config.identificador_concepto
                        codigo_barras += str(code_config.id).zfill(8)
                        codigo_barras += fecha_1er_vto
                        codigo_barras += importe_1er_vto
                        codigo_barras += str(rec.dias_2do_vto).zfill(2)
                        codigo_barras += importe_2do_vto
                        codigo_barras += str(rec.dias_3do_vto).zfill(2)
                        codigo_barras += importe_3er_vto
                        codigo_barras += code_config.identificador_cuenta
                    suma_de_productos = 0
                    i = 0
                    for digito in SECUENCIA_VERIFICADORA:
                        if i < codigo_barras.__len__():
                            suma_de_productos += digito * int(codigo_barras[i])
                            i += 1
                    primer_digito_verificador = math.trunc(suma_de_productos / 2)
                    primer_digito_verificador = primer_digito_verificador % 10
                    codigo_barras += str(primer_digito_verificador)
                    suma_de_productos = suma_de_productos + primer_digito_verificador * DIGITO_VERIFICADOR_ADICIONAL
                    segundo_digito_verificador = math.trunc(suma_de_productos / 2)
                    segundo_digito_verificador = segundo_digito_verificador % 10
                    codigo_barras += str(segundo_digito_verificador)
                    rec.codigo_barra = codigo_barras
                except Exception as e:
                    print(e)
