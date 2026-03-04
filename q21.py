import pandas as pd

data = {"Name":["Apple","Banana","Mango"]}

df = pd.DataFrame(data)

df["Name"] = df["Name"].str.swapcase()

print(df)
