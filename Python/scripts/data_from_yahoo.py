#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

"""
In order to run this or almost any other Python script,
the user needs to be able to load/install 3rd-party Python modules/packages from the internet.

There are many ways to do this; we will propose one way:

Install Python IDE/Debugger called Spyder as a part of a bigger package called Anaconda.

First, download and install Anaconda from https://www.anaconda.com/products/individual

Then launch Anaconda and install Spyder in-app from https://docs.spyder-ide.org/current/installation.html

After that, follow the instructions on https://stackoverflow.com/questions/10729116/adding-a-module-specifically-pymorph-to-spyder-python-ide
and run the command:

pip install pandas_datareader

If you need to load/install other Python 3rd-party packages, then run:
pip install "name of package"
Example:
pip install numpy
pip install pandas

This script downloads and prints daily OHLCV data for the given instruments.
"""

from pandas_datareader import data as pdr
import yfinance as yf
import datetime

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

    # Validate date format
    try:
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
        datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD")
    else:
        fetch_yfinance_data(start_date, end_date, 'MSFT', 'IWO', 'VFINX', 'BTC-USD')
