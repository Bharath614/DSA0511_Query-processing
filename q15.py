import pandas as pd
import numpy as np

data = {"A":[1,np.nan,np.nan,4],
        "B":[np.nan,np.nan,3,4],
        "C":[1,2,np.nan,np.nan]}

df = pd.DataFrame(data)

result = df[df.isnull().sum(axis=1) >= 2]

print(result)
