from dataclasses import dataclass

from .data_request import DataRequest


@dataclass
class StockQuoteRequest(DataRequest):
    """ Data model for stock quote requests. Also works for etf and indices """
    ticker: str
    start_date: str = None
    end_date: str = None
