import numpy as np
import pandas as pd


np.random.seed(0)
df = pd.DataFrame({
    "before": np.random.normal(90, 10, 16),
    "after": np.random.normal(85, 10, 16)
})

df.head(n=8).to_csv("do1.csv", index=False)
df.tail(n=8).to_csv("do2.csv", index=False)
