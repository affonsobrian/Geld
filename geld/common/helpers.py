import json
from decimal import Decimal


class AsynClientHelper:
    @staticmethod
    async def get_rate_from_response(response: dict, to_currency: str):
        text = await response.text()
        data = json.loads(text)
        rate = Decimal(data["rates"][to_currency])
        return rate
