import pandas as pd

data = {"Name":["Apple","Banana","Mango","Grapes"]}

df = pd.DataFrame(data)

result = df["Name"].str.find("an")

print(result)
