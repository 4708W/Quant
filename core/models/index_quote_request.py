from dataclasses import dataclass

from .data_request import DataRequest


@dataclass
class IndexQuoteRequest(DataRequest):
    ticker: str
    start_date: str
    end_date: str
