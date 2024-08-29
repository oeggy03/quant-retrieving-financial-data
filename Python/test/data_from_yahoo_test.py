import unittest

from Python.src.info_retreival.data_from_yahoo import fetch_yfinance_data


class TestFetchYFinanceData(unittest.TestCase):

    def test_valid_symbols_and_dates(self):
        # Test with valid symbols and valid date range
        start_date = '2023-09-25'
        end_date = '2023-10-02'
        symbols = ['MSFT', 'IWO', 'VFINX', 'BTC-USD']
        fetch_yfinance_data(start_date, end_date, *symbols)

    def test_invalid_symbols(self):
        # Test with some invalid symbols
        start_date = '2023-09-25'
        end_date = '2023-10-02'
        symbols = ['INVALID1', 'INVALID2']
        fetch_yfinance_data(start_date, end_date, *symbols)

    def test_mixed_valid_and_invalid_symbols(self):
        # Test with a mix of valid and invalid symbols
        start_date = '2023-09-25'
        end_date = '2023-10-02'
        symbols = ['MSFT', 'INVALID']
        fetch_yfinance_data(start_date, end_date, *symbols)

    def test_empty_symbols(self):
        # Test with no symbols
        start_date = '2023-09-25'
        end_date = '2023-10-02'
        symbols = []
        fetch_yfinance_data(start_date, end_date, *symbols)

    def test_invalid_date_format(self):
        # Test with invalid date format
        start_date = '2023-25-09'
        end_date = '2023-02-10'
        symbols = ['MSFT']
        with self.assertRaises(ValueError):
            fetch_yfinance_data(start_date, end_date, *symbols)

    def test_end_date_before_start_date(self):
        # Test with end date before start date
        start_date = '2023-10-02'
        end_date = '2023-09-25'
        symbols = ['MSFT']
        fetch_yfinance_data(start_date, end_date, *symbols)


if __name__ == "__main__":
    unittest.main()
