import pandas as pd

data = {"school_code":["s001","s001","s002","s002","s003"],
        "class":[5,6,5,6,5],
        "name":["John","Sara","Mike","David","Anna"]}

df = pd.DataFrame(data)

grouped = df.groupby(["school_code","class"])

print(grouped.size())
