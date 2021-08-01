from quant.factories import StockDataGetterFactory, Provider
from quant.models import StockQuoteRequest

# create stock data getter using factory
stock_data_getter = StockDataGetterFactory.create(Provider.ALPHA_VANTAGE)

# retrieve stock quote series
request = StockQuoteRequest(ticker="VNQ")
vnq = stock_data_getter.get_stock_daily_adjusted(request)

request = StockQuoteRequest(ticker="SPY")
spy = stock_data_getter.get_stock_daily_adjusted(request)

print(vnq)
print(spy)

