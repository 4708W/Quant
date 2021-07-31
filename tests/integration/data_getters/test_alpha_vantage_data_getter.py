import pytest

from core.data_getters import AlphaVantageDataGetter
from core.models import StockQuoteRequest


@pytest.mark.parametrize("ticker", ["VNQ", "SPXU", "SQQQ", "PSQ"])
def test_get_stock_daily_adjusted_when_given_valid_request_should_work(ticker):
    alpha_vantage_data_getter = AlphaVantageDataGetter()
    request = StockQuoteRequest(ticker=ticker)
    daily_adjusted_series = alpha_vantage_data_getter.get_stock_daily_adjusted(request)
    print(daily_adjusted_series)
