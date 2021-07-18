from dataclasses import dataclass

from .data_request import DataRequest


@dataclass
class StockQuoteRequest(DataRequest):
    ticker: str
<<<<<<< HEAD
    start_date: str = None
    end_date: str = None
=======
    start_date: str
    end_date: str
>>>>>>> add data getters
