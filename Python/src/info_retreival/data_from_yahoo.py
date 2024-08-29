import datetime
import yfinance as yf
from pandas_datareader import data as pdr
import unittest

yf.pdr_override()


def fetch_yfinance_data(start_date, end_date, *symbols):
    """
    Fetches OHLCV data for the given symbols from Yahoo Finance.

    Parameters:
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.
    symbols (tuple): Tuple of stock/ETF/mutual fund/currency symbols.

    Returns:
    None
    """
    # Validate date format
    try:
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
        datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    for symbol in symbols:
        try:
            print(f">> {symbol} ... ", end='')
            data = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)
            print(data)
        except Exception as e:
            print(f"Failed to retrieve data for {symbol}: {e}")


if __name__ == "__main__":
    start_date = '2023-09-25'
    end_date = '2023-10-02'

    try:
        fetch_yfinance_data(start_date, end_date, 'MSFT', 'IWO', 'VFINX', 'BTC-USD')
    except Exception as e:
        print(e)
