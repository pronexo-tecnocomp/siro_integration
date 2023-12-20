16.0.1 (16nd Nov 2023)
----------------------

- Initial release

16.2.1 (17nd Nov 2023)
----------------------

- Se agregaron views y models para la config


16.3.1 (21nd Nov 2023)
----------------------

- Cambios en la generación del codigo de barras
- Siro_id y views

16.4.1 (6th Dec 2023)
----------------------
- siro.config -> Solo Form View
- siro.config -> Trae el ultimo registro guardado al cargar la form view

16.5.1 (19th Dec 2023)
----------------------
- Agregado de Reporte de Boleta de Pago
- Agregado de sequencia para el reporte de "Boleta de Pago"
- Oculacion de campos de Siro si la factura es distinta a out_invoice

16.6.1 (20th Dec 2023)
----------------------
- Campos de tipo boolean para la comprobacion de si la factura esta paga y si es un abono de siro
- Se puede imprimir el reporte de Boleta de Pago si el campo de abono_siro es True
- Marca en el reporte de boleta de pago si no esta paga la factura como "DEUDADO"
