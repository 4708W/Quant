import pytest
from core.data_getters.yahoo_finance_index_quote_getter import YahooFinanceIndexQuoteGetter
from core.models import IndexQuoteRequest, IndexQuote


def test_get_when_given_explicit_start_and_end_should_work():
    # todo: this test could be a test for index_quote_getter instead of for yahoo finance index
    #  quote getter only. What can be done is to provide a getter engine to index_quote_getter
    #  so that the IndexQuoteGetter can switch the data source easily
    request = IndexQuoteRequest(ticker="SPX", start_date="2018-01-01", end_date="2018-03-01")
    index_quote_series = YahooFinanceIndexQuoteGetter.get(request)
    for quote in index_quote_series:
        assert isinstance(quote, IndexQuote)
