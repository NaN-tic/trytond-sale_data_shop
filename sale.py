# This file is part sale_data_shop module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

    @classmethod
    def get_sale_data(self, party, description=None):
        '''Add shop in sale object'''
        User = Pool().get('res.user')
        user = User(Transaction().user)

        sale = super(Sale, self).get_sale_data(party, description)
        if user.shop:
            sale.shop = user.shop.id
        return sale
