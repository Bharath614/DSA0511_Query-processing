import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker = "GOOGL" 

start_date = "2023-01-01"
end_date = "2023-12-31"

df = yf.download(ticker, start=start_date, end=end_date)

plt.figure()
plt.plot(df.index, df["Close"])
plt.title("Alphabet Inc. (GOOGL) Stock Price")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.xticks(rotation=45)
plt.show()