# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ComprasProveedor(models.Model):
    _name = 'compras.proveedor'
    name = fields.Char(string="Nombre proveedor", required=True)
    region = fields.Selection([('7region', 'VII Región del Maule'),
                               ('other_region', 'Otra región')], string="Región", required=True)
    city = fields.Char(string="Ciudad", required=True)
    business_category = fields.Selection(
        [('librery', 'Artículos de Librería'), ('music', 'Artículos musicales'),
         ('cleaning', 'Artículos de aseo'), ('other', 'Otros')], string="Rubro/Giro", required=True)
    email = fields.Char(string="Correo electrónico", required=True)
    phone_number = fields.Integer(string="Número de teléfono", required=True)
    website = fields.Char(string="Sitio Web")
    producto_ids = fields.One2many(
        'compras.producto', 'proveedor_id', string="Productos")
    total_productos = fields.Integer(
        string="Total de productos", compute="_total_productos")

    @api.one
    def _total_productos(self):
        self.total_productos = len(self.producto_ids)
    
    order_id = fields.Many2one(
        'compras.ordencompra','proveedor_ids')



class ComprasProducto(models.Model):
    _name = 'compras.producto'
   # supplier=fields.Char(string="Nombre de proveedor", required=True)
    name = fields.Char(string="Nombre producto", required=True)
    price = fields.Integer(string="Precio unitario",
                           widget="monetary", required=True)

    description = fields.Char(string="Descripción del producto")
    proveedor_id = fields.Many2one(
        'compras.proveedor', string="Proveedor", required=True)
    detalle_id=fields.Many2one('compras.detallecompra', 'producto_ids')


class DetalleCompra(models.Model):
 _name = 'compras.detallecompra'
 producto_ids=fields.One2many(
     'compras.producto', 'detalle_id', string="Productos")
 order_id=fields.Many2one('compras.ordencompra', 'detalle_ids')
 
 
 


class ComprasOrdenDeCompra(models.Model):
    _name = 'compras.ordencompra'
    name=fields.Char("Orden de Compra")
    date_order = fields.Date(string="Fecha Orden de compra", required=True)
    notes = fields.Char(string="Comentarios")
    #proveedor_ids = fields.One2many(
     #   'compras.proveedor', 'order_id', string="Proveedor")
    detalle_ids=fields.One2many('compras.detallecompra', 'order_id')
    #total_proveedores = fields.Integer(string="Total Proveedores", compute="_total_proveedores") 
    #@api.one
    #def _total_proveedores(self):
     
     #   self.total_proveedores =len(self.proveedor_ids) 
    proveedor_id = fields.Many2one('compras.proveedor', string="nombre proveedor")

