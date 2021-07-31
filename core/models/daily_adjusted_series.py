from dataclasses import dataclass

from .data_series import DataSeries


@dataclass
class DailyAdjustedSeries(DataSeries):
    ticker: str
    start_date: str
    end_date: str
