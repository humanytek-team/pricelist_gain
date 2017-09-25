from odoo import api, fields, models


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    gain = fields.Float(
        compute='_get_gain', readonly=False,
    )
    price_discount = fields.Float('Price Discount', default=0, digits=(16, 2), compute='_get_price_discount', store=True, readonly=False)

    @api.depends('price_discount')
    @api.multi
    def _get_gain(self):
        for r in self:
            r.gain = 100*r.price_discount / (r.price_discount - 100)

    @api.depends('gain')
    @api.multi
    def _get_price_discount(self):
        for r in self:
            r.price_discount = 100*r.gain / (r.gain - 100)
