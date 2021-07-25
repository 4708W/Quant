from .data_getter import DataGetter
from core.models import StockQuoteRequest
import requests


class AlphaVantageDataGetter(DataGetter):

    def __init__(self):
        super().__init__(environment_variable="ALPHA_VANTAGE_API_KEY")

    def get_stock_daily_adjusted(self, request: StockQuoteRequest):
        """ get daily adjusted time series data for the given stock data request """
        url = "https://www.alphavantage.co/query"
        query_param = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": request.ticker,
            # "outputsize": "full",
            "apikey": self.api_key
        }
        response = requests.get(url, params=query_param)
        return response.json()
