import yfinance as yf
import pandas as pd
from datetime import datetime

def download_nvda(start_date: str = "2019-01-01", end_date: str = None):
    """
    Download NVIDIA historical data from Yahoo Finance.
    Returns a DataFrame with Date as index and all OHLCV columns.
    """
    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")
    ticker = "NVDA"
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    df.index = pd.to_datetime(df.index)
    return df

if __name__ == "__main__":
    df_nvda = download_nvda()
    df_nvda.to_csv("../data/yfinance_nvda.csv")
    print("Downloaded data:", df_nvda.shape)
