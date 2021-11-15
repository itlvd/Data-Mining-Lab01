import pandas as pd
import sys


def min_max(df):
    for col in range(1,df.shape[1]):
        x = df.iloc[:,col]
        if(x.dtype in ['O','S','U','V']):
            continue
        df.iloc[:,col] = x.astype(float)
        df.iloc[:,col] = (x - min(x)) / ((max(x) - min(x)) > 0 and (max(x) - min(x)) or len(x))
    return df

src='house-prices.csv'
df = pd.read_csv(src)
d_d =min_max(df)
print(d_d)

