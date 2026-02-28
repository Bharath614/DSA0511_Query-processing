import yfinance as yf
import matplotlib.pyplot as plt

ticker = "GOOGL"
start_date = "2023-01-01"
end_date = "2023-03-31"

df = yf.download(ticker, start=start_date, end=end_date)

if isinstance(df.columns, tuple) or hasattr(df.columns, "levels"):
    df.columns = df.columns.get_level_values(0)

df = df.reset_index()

plt.figure()
plt.bar(df["Date"], df["Volume"].astype(float))

plt.title("Alphabet Inc. (GOOGL) Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.xticks(rotation=45)

plt.show()