import pandas as pd

data = {"Year":[2018,2019,2020],
        "Country":["India","USA","UK"],
        "Consumption":[10,15,7]}

df = pd.DataFrame(data)

print(df.shape)
print(df.columns)
