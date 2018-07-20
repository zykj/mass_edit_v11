# -*- coding: utf-8 -*-
# © 2016 Serpent Consulting Services Pvt. Ltd. (support@serpentcs.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


import logging
_logger = logging.getLogger(__name__)


class IrModelFields(models.Model):
    _inherit = 'ir.model.fields'

    @api.model
    def search(self, args, offset=0, limit=0, order=None, count=False):
        model_domain = []
        # _logger.debug("------- intial domain ---------")
        for domain in args:

            # _logger.info(domain)
            
            if (len(domain) > 2 and domain[0] == 'model_id' and
                    isinstance(domain[2], str) and
                    list(domain[2][1:-1])):
                try:
                   model_domain += [('model_id', 'in',
                                  map(int, domain[2][1:-1].split(',')))]
                except ValueError as e:
                    # _logger.info(str(e))
                    continue
            else:
                model_domain.append(domain)
        # _logger.debug("------- final domain ---------")
        # _logger.debug(model_domain)
        return super(IrModelFields, self).search(model_domain, offset=offset,
                                                 limit=limit, order=order,
                                                 count=count)
