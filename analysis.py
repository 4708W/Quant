from tests.unit.data_getters.data_reader import DataReader
import pandas as pd
from dateutil import parser

TIMES_SERIES_DAILY = "Time Series (Daily)"

OPEN = "OPEN"
HIGH = "HIGH"
LOW = "LOW"
CLOSE = "CLOSE"
ADJUSTED_CLOSE = "ADJUSTED_CLOSE"
VOLUME = "VOLUME"
DIVIDEND_AMOUNT = "DIVIDEND_AMOUNT"
SPLIT_COEFFICIENT = "SPLIT_COEFFICIENT"

ALPHA_VANTAGE_TIME_SERIES_COLUMN_MAPPING = {
    "1. open": OPEN,
    "2. high": HIGH,
    "3. low": LOW,
    "4. close": CLOSE,
    "5. adjusted close": ADJUSTED_CLOSE,
    "6. volume": VOLUME,
    "7. dividend amount": DIVIDEND_AMOUNT,
    "8. split coefficient": SPLIT_COEFFICIENT
}


def load_time_series_dataframe_from_test_data(ticker) -> pd.DataFrame:
    """ read stock data from test folder and load as dataframe """
    data = DataReader.read(f"{ticker}.json")
    time_series_dataframe = pd.DataFrame(data.get(TIMES_SERIES_DAILY)).T
    return time_series_dataframe.rename(columns=ALPHA_VANTAGE_TIME_SERIES_COLUMN_MAPPING)


def load_adjusted_close_time_series_dataframe_from_test_data(ticker) -> pd.DataFrame:
    time_series_dataframe = load_time_series_dataframe_from_test_data(ticker)
    adjusted_close_series = time_series_dataframe[ADJUSTED_CLOSE].astype(float)
    adjusted_close_series.name = ticker
    return adjusted_close_series


def report(content, title):
    # todo: create a report builder
    print("\n")
    print(title)
    print("----------------------------------------------------")
    print(content)


if __name__ == "__main__":
    vnq = load_adjusted_close_time_series_dataframe_from_test_data("vnq")
    spxu = load_adjusted_close_time_series_dataframe_from_test_data("spxu")
    sqqq = load_adjusted_close_time_series_dataframe_from_test_data("sqqq")
    psq = load_adjusted_close_time_series_dataframe_from_test_data("psq")

    # correlation matrix
    adj_close = pd.DataFrame([vnq, spxu, sqqq, psq]).T
    adj_close = adj_close.sort_index()
    adj_close_return = adj_close.pct_change()
    variance_covariance_matrix = adj_close_return.corr()
    report(variance_covariance_matrix, "Variance-Covariance Matrix")

    # annualized return
    historical_return = adj_close_return.mean()
    # days_in_time_series = parser.parse(adj_close.index[0]) - parser.parse(adj_close.index[-1])
    annualized_return = historical_return * (255)
    report(annualized_return, "Annualized Return")

    # volatility
    volatility_daily = adj_close_return.std()
    annualized_volatility = volatility_daily * (255 ** 0.5)
    report(annualized_volatility, "Annualized Volatility")

    # price chart
