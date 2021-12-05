from geld.common.constants import BASE_URL
from geld.common.decorators import validate_currency_conversion_data
from geld.sync.base import SyncClientBase

from decimal import Decimal

class SyncClient(SyncClientBase):
    _base_url = BASE_URL

    @validate_currency_conversion_data
    def convert_currency(self, from_currency: str, to_currency: str, amount: Decimal = 1, date: str = "latest"):
        return super(SyncClient, self).convert_currency(from_currency, to_currency, amount, date)
