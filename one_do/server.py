import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import pandas as pd

def main():
    df1 = pd.read_csv("data1.csv")
    print(f"The sum is : {df1["number"].sum()}")


if __name__ == "__main__":
    main()
