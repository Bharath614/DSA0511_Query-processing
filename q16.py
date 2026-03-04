import pandas as pd

data = {"school_code":["s001","s002","s001","s002","s003"],
        "class":[5,6,5,6,5],
        "name":["John","Mike","Sara","David","Anna"],
        "age":[12,13,12,13,11]}

df = pd.DataFrame(data)

grouped = df.groupby("school_code")

print(type(grouped))
