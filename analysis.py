from tests.unit.data_getters.data_reader import DataReader
import pandas as pd
import matplotlib.pyplot
import io
import base64

matplotlib.pyplot.ioff()
matplotlib.pyplot.rcParams.update({'font.size': 8})
pd.set_option('display.width', 1000)
pd.set_option('colheader_justify', 'center')

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

pd.options.display.html.border = 0


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


def fig_to_base64(fig):
    img = io.BytesIO()
    fig.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    return base64.b64encode(img.getvalue())


def report(content, title):
    # todo: create a report builder
    print("\n")
    print(title)
    print("----------------------------------------------------")
    print(content)


def add_section(section_title):
    return rf"<p><strong>{section_title}</strong><br /></p>"


def build_html_table(dataframe):
    html_string = '''
        <html>
          <head><title>HTML Pandas Dataframe with CSS</title></head>
          <link rel="stylesheet" type="text/css" href="df_style.css"/>
          <body>
            {table}
          </body>
        </html>
    '''
    return html_string.format(table=dataframe.to_html(classes='mystyle'))


if __name__ == "__main__":

    vnq = load_adjusted_close_time_series_dataframe_from_test_data("vnq")
    spxu = load_adjusted_close_time_series_dataframe_from_test_data("spxu")
    sqqq = load_adjusted_close_time_series_dataframe_from_test_data("sqqq")
    psq = load_adjusted_close_time_series_dataframe_from_test_data("psq")

    # html  todo: create HTML Report builder
    html = ""

    # correlation matrix
    adj_close = pd.DataFrame([vnq, spxu, sqqq, psq]).T
    adj_close = adj_close.sort_index()
    adj_close_return = adj_close.pct_change()  # todo: use log to calculate changes
    variance_covariance_matrix = adj_close_return.corr()
    report(variance_covariance_matrix, "Variance-Covariance Matrix")

    html += add_section("Variance-Covariance Matrix")
    html += build_html_table(variance_covariance_matrix)

    # annualized return
    historical_return = adj_close_return.mean()
    # days_in_time_series = parser.parse(adj_close.index[0]) - parser.parse(adj_close.index[-1])
    annualized_return = historical_return * (255)
    report(annualized_return, "Annualized Return")
    html += add_section("Annualized Return")
    html += build_html_table(pd.DataFrame(annualized_return, columns=["Return"]))

    # volatility
    volatility_daily = adj_close_return.std()
    annualized_volatility = volatility_daily * (255 ** 0.5)
    report(annualized_volatility, "Annualized Volatility")
    html += add_section("Annualized Volatility")
    html += build_html_table(pd.DataFrame(annualized_volatility, columns=["Volatility"]))

    # relative value
    normalized_price = pd.DataFrame()
    for ticker in adj_close:
        start_date = adj_close.index.min()
        normalized_price[ticker] = adj_close[ticker] / adj_close.loc[start_date, ticker]

    ax = normalized_price.plot(figsize=(6, 3), title="Net Value Trend")
    fig = ax.get_figure()

    # generate report
    encoded = fig_to_base64(fig)
    html += add_section("Net Value Trend")
    html += '<img src="data:image/png;base64, {}">'.format(encoded.decode('utf-8'))

    # save report.html
    with open("report.html", "w+") as f:
        f.write(html)
