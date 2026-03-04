import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("fdata.csv")

plt.plot(df["Date"],df["Open"])
plt.plot(df["Date"],df["High"])
plt.plot(df["Date"],df["Low"])
plt.plot(df["Date"],df["Close"])
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Financial Data")
plt.xticks(rotation=45)
plt.show()
