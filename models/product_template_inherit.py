# -*- coding: utf-8 -*-
# Copyright 2018 Roland NEYRINCK
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, exceptions


class ProductTemplate(models.Model):
    _inherit = "product.template"

    visible_for_customer = fields.Boolean(string='Visible pour le client ?', default=False)


