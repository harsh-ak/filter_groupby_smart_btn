from odoo import api, fields, models, _, tools
from odoo.osv import expression
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit="sale.order"


    total_lines=fields.Integer("Total Lines",compute="total_liness")

    def count_lines(self):
        print("----------------------selfffffffffffffffff",self)
        for rec in self.order_line:
            print("______product idssss-----------",rec.product_id.ids)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Products',
            'view_mode': 'tree',
            'res_model': 'product.product',
            'domain': [('id', '=', self.order_line.product_id.ids)],
            # 'context': "{'create': False}"
        }

    

    @api.depends('order_line')    
    def total_liness(self):
        cnt=0
        for rec in self:
            lines=len(rec.order_line.ids)

        self.total_lines=lines

            