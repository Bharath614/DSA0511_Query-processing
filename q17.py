import pandas as pd

data = {"school_code":["s001","s002","s001","s002","s003"],
        "age":[12,13,14,15,11]}

df = pd.DataFrame(data)

result = df.groupby("school_code")["age"].agg(["mean","min","max"])

print(result)
