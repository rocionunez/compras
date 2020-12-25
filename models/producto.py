# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ComprasProveedor(models.Model):
    _name = 'compras.proveedor'
    name = fields.Char(string="Nombre proveedor", required=True)
    region = fields.Selection([('7region', 'VII Región del Maule'),
                               ('other_region', 'Otra región')], string="Región", required=True)
    city = fields.Char(string="Ciudad", required=True)
    business_category = fields.Selection(
        [('librery', 'Artículos de Librería'), ('music', 'Artículos musicales'),
         ('cleaning', 'Artículos de aseo'), ('art', 'Artículos artísticos'), ('other', 'Otros')], string="Rubro/Giro", required=True)
    email = fields.Char(string="Correo electrónico", required=True)
    phone_number = fields.Integer(string="Número de teléfono", required=True)
    website = fields.Char(string="Sitio Web")
    order_id = fields.Many2one(
        'compras.ordencompra', 'proveedor_ids')


class ComprasProducto(models.Model):
    _name = 'compras.producto'
    detalle_id = fields.Many2one('compras.detallecompra', 'producto_ids')


class ComprasOrdenDeCompra(models.Model):
    _name = 'compras.ordencompra'
    name = fields.Char("Referencia Interna", required=True)
    date_order = fields.Date(string="Fecha Orden de compra", default=fields.Date.context_today, required=True, readonly=True)
    notes = fields.Char(string="Comentarios")
    detalle_ids = fields.One2many('compras.detallecompra', 'order_id')
    proveedor_id = fields.Many2one(
        'compras.proveedor', string="Nombre Proveedor", required=True)
    _sql_constraints = [('name', 'unique(name)', 'Referencia interna de Orden de compra ya existe')
                        ]


class DetalleCompra(models.Model):
    _name = 'compras.detallecompra'
    producto_ids = fields.One2many(
        'compras.producto', 'detalle_id', string="Productos")
    order_id = fields.Many2one('compras.ordencompra', 'detalle_ids')
    name = fields.Char(string="Nombre producto", required=True)
    price = fields.Integer(string="Precio unitario",
                           widget="monetary", required=True)
    qtty = fields.Integer(string="Cantidad", required=True, default=1)
    description = fields.Char(string="Descripción del producto")
    total = fields.Integer(string="Total", compute="_total")

    @api.onchange('qtty')
    @api.depends('qtty')
    def validar_cantidad(self):
        if self.qtty < 1:
            raise ValidationError("La cantidad no puede ser menor a 1")

    @api.one
    def _total(self):
        self.total = (self.qtty * self.price)
