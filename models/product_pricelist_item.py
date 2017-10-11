from odoo import api, fields, models


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    gain = fields.Float(
        compute='_get_gain', readonly=False,
    )
    iar = fields.Float()
    term_months = fields.Float()
    fir = fields.Float(
        compute="_get_fir"
    )

    @api.one
    @api.depends('iar', 'term_months')
    def _get_fir(self):
        self.fir = (self.iar/100)*self.term_months/12

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
