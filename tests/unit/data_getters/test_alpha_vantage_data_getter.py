import pytest
from unittest.mock import patch
from pathlib import Path

from core.data_getters import AlphaVantageDataGetter
from core.models import DailyAdjustedRequest
import core.data_getters.alpha_vantage_data_getter
import json


@pytest.fixture
def alpha_vantage_data_getter():
    return AlphaVantageDataGetter()


def read_test_data(file_name: str):
    data_dir = Path(__file__).parent / Path("data")



@patch.object(alpha_vantage_data_getter, "requests")
def test_get_stock_daily_adjusted_when_api_request_mocked_when_given_valid_request_should_work(
        mock, alpha_vantage_data_getter
):
    mock.json.return_value = json.l
    request = DailyAdjustedRequest(ticker="IBM", start_date="2021-07-01", end_date="2021-07-25")
    daily_adjusted_series = alpha_vantage_data_getter.get_stock_daily_adjusted(request)
    print(daily_adjusted_series)