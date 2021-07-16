from abc import ABC, abstractmethod
from core.models import DataRequest


class DataGetter(ABC):
    @abstractmethod
    def get(self, request: DataRequest):
        pass
