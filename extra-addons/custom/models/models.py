# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustoSaleOrder(models.Model):
    _inherit = 'sale.order'

    lista = fields.Selection([('l1','Lista 1'),('l2','Lista 2')],string='Tipo')

