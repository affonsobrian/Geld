from decimal import Decimal
from unittest.mock import Mock, patch
from geld import __version__


def test_version():
    assert __version__ == "0.3.0"

def test_full_cycle_test():
    from geld.clients import sync_client
    expected_result = Decimal("5.43")
    response_mock = Mock(
        status_code = 200,
        text = '{"rates": {"BRL": "5.43"}}'
    )
    with patch("geld.sync.base.requests.get", return_value=response_mock):
        result = sync_client.convert_currency("USD", "BRL", 1)
    
    assert result == expected_result