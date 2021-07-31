from dataclasses import dataclass

from .data_request import DataRequest


@dataclass
class StockQuoteRequest(DataRequest):
    ticker: str
    start_date: str = None
    end_date: str = None
