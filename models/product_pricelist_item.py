from odoo import api, fields, models


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    gain = fields.Float(
        compute='_get_gain', readonly=False,
    )
    price_discount = fields.Float('Price Discount', default=0, digits=(16, 2), compute='_get_price_discount', store=True, readonly=False)

    @api.depends('price_discount')
    @api.one
    def _get_gain(self):
        self.gain = 100*self.price_discount / (self.price_discount - 100)

    @api.depends('gain')
    @api.one
    def _get_price_discount(self):
        self.price_discount = 100*self.gain / (self.gain - 100)
