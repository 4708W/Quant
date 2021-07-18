from dataclasses import dataclass


@dataclass
class IndexQuote:
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    dividends: float  # todo: check whether float makes sense
    stock_splits: float  # todo: check whether float makes sense
