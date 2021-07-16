import yfinance  # package that provide access to Yahoo Finance
from typing import List

from core.data_getters.data_getter import DataGetter
from core.models import IndexQuoteRequest, IndexQuote


class YahooFinanceIndexQuoteGetter(DataGetter):

    OPEN = "Open"
    HIGH = "High"
    LOW = "Low"
    CLOSE = "Close"
    VOLUME = "Volume"
    DIVIDENDS = "Dividends"
    STOCK_SPLITS = "Stock Splits"

    @staticmethod
    def get(request: IndexQuoteRequest) -> List[IndexQuote]:
        """ request data based on given request """
        ticker = yfinance.Ticker(request.ticker)
        data = ticker.history(start=request.start_date, end=request.end_date)
        index_quote_series = YahooFinanceIndexQuoteGetter._convert_to_index_quote_series(data)
        return index_quote_series

    @classmethod
    def _convert_to_index_quote_series(cls, data) -> List[IndexQuote]:
        index_quote_series = []
        for idx, row in data.iterrows():
            index_quote_series.append(
                IndexQuote(
                    date=idx.strftime("%Y-%m-%d"),
                    open=row[cls.OPEN],
                    high=row[cls.HIGH],
                    low=row[cls.LOW],
                    close=row[cls.CLOSE],
                    volume=row[cls.VOLUME],
                    dividends=row[cls.DIVIDENDS],
                    stock_splits=row[cls.STOCK_SPLITS],
                )
            )
        return index_quote_series
