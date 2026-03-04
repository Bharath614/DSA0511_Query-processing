import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4), columns=["A","B","C","D"])

df.iloc[1,2] = np.nan
df.iloc[4,0] = np.nan
df.iloc[7,3] = np.nan

print(df.isnull())
