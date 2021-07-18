from .provider import Provider
from core.data_getters.alpha_vantage_data_getter import AlphaVantageDataGetter


class StockDataGetterFactory:
    """ factory method that create a concrete stock data getter based on given provider """

    @staticmethod
    def create(provider: Provider):
        """ Create a stock data getter based on given provider"""
        if provider == Provider.ALPHA_VANTAGE:
            return AlphaVantageDataGetter()
        else:
            raise ValueError("Invalid data provider")
