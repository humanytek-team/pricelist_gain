from odoo import api, fields, models


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    gain = fields.Float(
        compute='_get_gain', readonly=False,
    )

    @api.depends('price_discount')
    @api.multi
    def _get_gain(self):
        for r in self:
            r.gain = 100*r.price_discount / (r.price_discount - 100)

    @api.onchange('gain')
    @api.multi
    def _get_price_discount(self):
        for r in self:
            r.price_discount = 100*r.gain / (r.gain - 100)
