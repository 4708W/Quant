from dataclasses import dataclass
from typing import List

from .stock_quote import StockQuote


@dataclass
class QuoteSeries:
    quotes: List[StockQuote]
