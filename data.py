import numpy as np
import pandas as pd

data = np.random.randint(1, 101, size=(5, 3))
df = pd.DataFrame(data, columns=["A", "B", "C"])
# df = dataframe 
df["Sum"] = df.sum(axis=1)g
df["Average"] = df[["A", "B", "C"]].mean(axis=1)

print(df)
