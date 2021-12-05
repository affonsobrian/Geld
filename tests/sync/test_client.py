from decimal import Decimal
import json
import pytest

from unittest.mock import MagicMock, Mock, patch
from geld.clients import sync_client
from geld.common.exceptions import APICallError


@pytest.mark.parametrize(
    "from_currency, to_currency, amount, date, rate",
    [
        ("USD", "BRL", 10, "2020-01-01", 5.50,),
        ("BRL", "USD", 5, "2021-01-01", 0.15,),
        ("USD", "EUR", 1, "2020-05-01", 0.97,),
    ]
)
@patch("geld.sync.client.SyncClient._execute_request")
def test_convert_currency_with_sync_client_success(execute_request_mock, from_currency, to_currency, amount, date, rate):
    expected_result = Decimal(amount) * Decimal(rate)
    response = Mock()
    response.status_code = 200
    response.text = json.dumps({
        'rates': {
            to_currency: rate
        }
    })
    execute_request_mock.return_value = response

    result = sync_client.convert_currency(from_currency, to_currency, amount, date)

    assert result == expected_result
    execute_request_mock.assert_called_once()


@pytest.mark.parametrize(
    "from_currency, to_currency, amount, date, rate",
    [
        ("USD", "BRL", 10, "2020-01-01", 5.50,),
        ("BRL", "USD", 5, "2021-01-01", 0.15,),
        ("USD", "EUR", 1, "2020-05-01", 0.97,),
    ]
)
@patch("geld.sync.client.SyncClient._execute_request")
def test_convert_currency_with_sync_client_request_fail(execute_request_mock, from_currency, to_currency, amount, date, rate):
    expected_result = Decimal(amount) * Decimal(rate)
    response = Mock()
    response.status_code = 404
    response.text = json.dumps({
        'rates': {
            to_currency: rate
        }
    })
    execute_request_mock.return_value = response

    with pytest.raises(APICallError):
        sync_client.convert_currency(from_currency, to_currency, amount, date)
