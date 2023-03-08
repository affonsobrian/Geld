from geld.common.exceptions import (
    APICallError,
    InvalidAmount,
    InvalidCurrencyCode,
    InvalidDate,
)
import pytest

from datetime import datetime
from decimal import Decimal
from unittest.mock import Mock, patch
from geld import __version__
from geld.clients import sync_client


def test_version():
    assert __version__ == "0.3.0"


@pytest.mark.parametrize(
    ("args", "expected_result"),
    [
        (["USD", "BRL", 1], Decimal("5.43")),
        (["USD", "BRL", 1, datetime.now()], Decimal("5.43")),
        (
            ["USD", "BRL", 1, datetime.isoformat(datetime.now())],
            Decimal("5.43"),
        ),
        (
            ["USD", "BRL", 10, datetime.isoformat(datetime.now())],
            Decimal("54.30"),
        ),
    ],
)
@patch(
    "geld.sync.base.requests.get",
    return_value=Mock(status_code=200, text='{"rates": {"BRL": "5.43"}}'),
)
def test_convert_currency_success(get_mock, args, expected_result):
    result = sync_client.convert_currency(*args)

    get_mock.assert_called_once()
    assert result == expected_result


@pytest.mark.parametrize(
    ("args", "expected_exception"),
    [
        (["USD", "BRL", -1], InvalidAmount),
        (["USD", "INVALID", 1], InvalidCurrencyCode),
        (["InvalidCurrencyCode", "BRL", 1], InvalidCurrencyCode),
        (["USD", "BRL", 1, "wrong-date"], InvalidDate),
    ],
)
@patch(
    "geld.sync.base.requests.get",
    return_value=Mock(status_code=200, text='{"rates": {"BRL": "5.43"}}'),
)
def test_convert_raise_exceptions(get_mock, args, expected_exception):
    with pytest.raises(expected_exception):
        _ = sync_client.convert_currency(*args)

    get_mock.assert_not_called()
