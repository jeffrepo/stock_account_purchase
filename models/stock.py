# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models

class StockMove(models.Model):
    _inherit = "stock.move"

    def _account_entry_move(self, qty, description, svl_id, cost):
        self.ensure_one()
        if self.picking_id.purchase_id.partner_id.disable_move:
            return False
        res = super(StockMove, self)._account_entry_move(qty=qty, description=description, svl_id=svl_id, cost=cost)
        return res
   


