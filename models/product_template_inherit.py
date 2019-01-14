# -*- coding: utf-8 -*-
# Copyright 2018 Roland NEYRINCK
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, exceptions


class ProductTemplate(models.Model):
    _inherit = "product.template"

    visible_for_customer = fields.Boolean(string='Visible pour le client ?', default=True, help='Si la case est cochee, ce produit sera visible sur le devis et la facture du client. A l inverse, si la case n est pas cochee, larticle sera comptabilise dans le montant total de la facture mais ne sera pas visible dans la liste des articles.')


