import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import requests
from datetime import datetime as dt

URL = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"

data = pd.read_html(requests.get(URL, headers={'User-agent': 'Mozilla/5.0'}).text,header=0)

# print(data[0].head())
# print(data[0].tail())

data[0]["Adj Close**"] = pd.to_numeric(data[0]["Adj Close**"], errors="coerce")
# print(data[0].tail())

data[0].dropna(inplace=True)
# print(data[0].tail())

data[0]["Date2"] = [dt.strptime(i, "%b %d, %Y") for i in data[0]["Date"]]
# print(data[0].tail())

data[0].set_index("Date2", inplace=True)
# print(data[0].head())
# print(data[0]["Adj Close**"].dtype)

plot1 = data[0]["Adj Close**"].plot(title="APPL Stock Price", grid=True)
# plt.show()
data[0].to_csv("AAPL_stock.csv")