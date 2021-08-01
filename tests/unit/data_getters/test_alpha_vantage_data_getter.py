import pytest
import responses

from core.data_getters import AlphaVantageDataGetter
from core.models import StockQuoteRequest
from .data_reader import DataReader


@pytest.fixture
def mock_alpha_vantage_response_vnq(mock_responses) -> responses.RequestsMock:
    mock_responses.add(
        method=responses.GET,
        url="https://www.alphavantage.co/query",
        json=DataReader.read("vnq.json"),
    )
    return mock_responses


def test_get_stock_daily_adjusted_when_given_valid_request_should_work(mock_alpha_vantage_response_vnq):
    alpha_vantage_data_getter = AlphaVantageDataGetter()
    request = StockQuoteRequest(ticker="VNQ")
    daily_adjusted_series = alpha_vantage_data_getter.get_stock_daily_adjusted(request)
    print(daily_adjusted_series)
