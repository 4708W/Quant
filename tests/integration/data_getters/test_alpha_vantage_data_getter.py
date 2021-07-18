import pytest

from core.data_getters import AlphaVantageDataGetter
from core.models import StockQuoteRequest


<<<<<<< HEAD
@pytest.mark.parametrize("ticker", ["VNQ", "SPXU", "SQQQ", "PSQ"])
def test_get_stock_daily_adjusted_when_given_valid_request_should_work(ticker):
    alpha_vantage_data_getter = AlphaVantageDataGetter()
    request = StockQuoteRequest(ticker=ticker)
=======
@pytest.fixture
def alpha_vantage_data_getter():
    return AlphaVantageDataGetter()


def test_get_stock_daily_adjusted_when_given_valid_request_should_work(alpha_vantage_data_getter):
    request = StockQuoteRequest(ticker="IBM", start_date="2021-07-01", end_date="2021-07-25")
>>>>>>> add data getters
    daily_adjusted_series = alpha_vantage_data_getter.get_stock_daily_adjusted(request)
    print(daily_adjusted_series)
