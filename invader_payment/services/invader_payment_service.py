# Copyright 2019 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.addons.component.core import Component


class InvaderPaymentService(Component):

    _name = "invader.payment.service"
    _inherit = "base.rest.service"
    _usage = "payment"

    def _invader_find_payable(self, target, **params):
        """
        # returns invader.payable
        :param params:
        :return:
        """
        raise NotImplementedError

    def _invader_get_target_validator(self):
        """
        Return a cerberus validator schema fragment that specifies the
        target being paid. Implementations must extend it by populating
        the "allowed" field (eg with strings such as 'current_cart') and
        possibly adding other fields.
        """
        return {
            "target": {"type": "string", "required": True, "allowed": []}
        }