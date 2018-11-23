# -*- coding: utf-8 -*-
# Copyright 2018 Roland NEYRINCK
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, exceptions


class SaleOrderLine(models.Model):
    _inherit = 'sale.order'

    customer_visible = fields.Boolean(related='product_id.visible_for_customer', string='Visible sur le devis')