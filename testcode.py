import pandas_datareader as web
from datetime import date, timedelta
import matplotlib.pyplot as plt
import mplfinance as mpf

start = (date.today() - timedelta(days=365)).strftime("%Y-%m-%d")  # get start date 1 year ago from today's date
end = date.today().strftime("%Y-%m-%d")  # get end date as today's date

nvda = web.DataReader("NVDA", "yahoo", start, end)
tesla = web.DataReader("TSLA", "yahoo", start, end)

fig, ax = plt.subplots()
ax.set_title("Stock Price Change YTD")
ax.plot(nvda["Close"], label="NVDA")
ax.plot(tesla["Close"] / tesla["Close"].iloc[0] * 100 - 100, label="Tesla")
ax.legend(["NVDA", "Tesla"])
mpf.make_addplot(
    nvda["Volume"] * 2e4, type="bar", ax=ax
)  # plot volume on secondary y axis with scale factor *2e4 to make it visible
plt.show()
