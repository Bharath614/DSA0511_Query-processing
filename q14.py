import pandas as pd
import numpy as np

data = {"ord_no":[70001,np.nan,70003,70004],
        "purch_amt":[150.5,270.65,np.nan,948.5]}

df = pd.DataFrame(data)

df = df.fillna(0)

print(df)
