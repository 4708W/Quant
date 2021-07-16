from abc import abstractmethod

from core.models import IndexQuoteRequest
from .data_getter import DataGetter


class IndexQuoteGetter(DataGetter):
    @abstractmethod
    def get(self, request: IndexQuoteRequest):
        pass
