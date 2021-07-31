from abc import abstractmethod, ABC

from core.models import DailyAdjustedRequest
import os


class DataGetter(ABC):
    """ base class of data getters for typing purpose """

    def __init__(self, environment_variable: str):
        self.api_key = os.environ.get(environment_variable)
        self.validate_api_key()

    def validate_api_key(self):
        """ validate that the api key is not empty """
        if not self.api_key:
            raise ValueError("Empty API key. Please store your api key in the environment variable.")

    @abstractmethod
    def get_stock_daily_adjusted(self, request: DailyAdjustedRequest):
        pass
