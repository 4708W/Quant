from abc import abstractmethod, ABC

from quant.models import StockQuoteRequest, QuoteSeries
import os


class DataGetter(ABC):
    """ base class of data getters for typing purpose """

    def __init__(self, environment_variable: str):
        self.environment_variable = environment_variable
        self.api_key = os.environ.get(environment_variable)
        self.validate_api_key()

    def validate_api_key(self):
        """ validate that the api key is not empty """
        if not self.api_key:
            raise ValueError(
                f"Environment variable {self.environment_variable} NOT found."
                f"Please store your api key in the environment variable with name {self.environment_variable}."
            )

    @abstractmethod
    def get_stock_daily_adjusted(self, request: StockQuoteRequest) -> QuoteSeries:
        pass
