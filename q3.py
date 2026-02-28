import pandas as pd

df = pd.read_excel("3.xlsx")

sorted_df = df.sort_values(by="JOB_TITLE", ascending=False)

print("Jobs in Descending Order of JOB_TITLE:\n")
print(sorted_df)