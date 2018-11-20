# -*- coding: utf-8 -*-
# Copyright 2018 Roland NEYRINCK
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "Facture pour les entreprises de la construction",
    'version': '10.0.1',
    'category': 'Generic Modules/Accounting',
    'author':   "Roland NEYRINCK",
    'website': '',
'description': """
        Le module ajoute un boolean sur la fiche de l'article pour indiquer si celui-ci doit être présent sur le devis du client (mais on 
        comptabilise bien le coût de celui-ci même s'il n'est pas affiché.
    """,
    'license': 'AGPL-3',
    "depends": [
        'account','sale'
    ],
    "data": [
        'views/product_view_inherit.xml',


    ],
    'installable': True,
}