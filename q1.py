import pandas as pd
df=pd.read_excel("1.xlsx")
depts_ids=df["DEPARTMENT_ID"].drop_duplicates()
print("Distinct Department ids:")
print(depts_ids)