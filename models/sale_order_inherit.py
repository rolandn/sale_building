# -*- coding: utf-8 -*-

# Copyright 2018 Roland NEYRINCK
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, exceptions


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    customer_visible = fields.Boolean(related='product_id.visible_for_customer', string='Visible sur le devis', default=True)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    comment_for_customer = fields.Char(string="Message pour le client", required=False, track_visibility='onchange')


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    customer_visible = fields.Boolean(related='product_id.visible_for_customer', string='Visible sur la facture', default=True)
