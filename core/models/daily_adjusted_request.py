from dataclasses import dataclass

from .data_request import DataRequest


@dataclass
class DailyAdjustedRequest(DataRequest):
    ticker: str
    start_date: str
    end_date: str
