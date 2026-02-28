import pandas as pd

df = pd.read_excel("2.xlsx")

job_counts = df.groupby("EMPLOYEE_ID").size()

employees_multiple_jobs = job_counts[job_counts >= 2].index

print("Employees who have done two or more jobs:")
print(list(employees_multiple_jobs))