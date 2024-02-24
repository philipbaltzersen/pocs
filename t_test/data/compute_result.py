import json
from pathlib import Path

import pandas as pd
import scipy.stats as sp

path = Path(__file__).parents[0]
df1 = pd.read_csv(path / "do1.csv")
df2 = pd.read_csv(path / "do2.csv")
df = pd.concat([df1, df2], axis=0)

result = sp.ttest_rel(df["after"], df["before"])

with open(path / "result.json", "w") as out_file:
    out_file.write(
        json.dumps(
            {
                "statistic": result.statistic,
                "pvalue": result.pvalue
            },
            indent=4
        )
    )
