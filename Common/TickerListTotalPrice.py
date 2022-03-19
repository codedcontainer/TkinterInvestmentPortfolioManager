from itertools import accumulate
import pandas as pd
from yahoo_finance_async import OHLC
from tkinter import messagebox

class TickerListTotalPrice():
    @staticmethod
    async def getTotalCurrentPriceAsync(tickers):
        closing_prices = []
        for ticker in tickers.split(","):
            try:
                result = await OHLC.fetch(symbol=ticker)                
                candle_count = len(result['candles'])
                closing_price = round(result['candles'][candle_count - 1]['close'],2)
                closing_prices.append(closing_price)
            except:
                pass
        return round(sum(closing_prices),2)

    @staticmethod
    async def closingPricesAsync(tickers):
        ticker_closing_prices = []
        for ticker in tickers.split(","):
            try:
                result = await OHLC.fetch(symbol = ticker)
                candle_count = len(result['candles'])
                closing_price = round(result['candles'][candle_count - 1]['close'],2)
                ticker_closing_prices.append({'ticker': ticker, 'closing_price': round(closing_price, 2)})
            except Exception:
                closing_price = 0
                messagebox.showerror(title="API Error", message='closing price for ticker {} does not exist'.format(ticker))
                pass
        df = pd.DataFrame.from_dict(ticker_closing_prices).sort_values(by='closing_price').reset_index()
        return df

    @staticmethod
    def accumulatedSum(closing_prices_dict):
        accumulated_sum = list(accumulate(closing_prices_dict['closing_price']))
        accumulated_sum = {'sum_price': [round(price, 2) for price in accumulated_sum]}
        accumulated_sum_df = pd.DataFrame(accumulated_sum)
        closing_prices_dict = pd.concat([accumulated_sum_df, closing_prices_dict], axis=1, join='inner')
        del closing_prices_dict['index']
        return closing_prices_dict

    @staticmethod
    def filterByAccountBalance(closing_prices_dict, account_balance):
        closing_prices_dict = closing_prices_dict[closing_prices_dict["sum_price"] <= account_balance]
        return [stock for stock in closing_prices_dict['ticker']]


