import pandas as pd


def delete_row_missing_value_rate(df,rate):
    head = df.columns
    num_col = round(rate / 100 * len(head))
    index_delete = []
    for row in range(df.shape[0]):
        count = 0
        for col in range(df.shape[1]):
            if pd.isnull(df.iat[row,col]):
                count+=1
                if count == num_col:
                    index_delete.append(row)
                    break
    df = df.drop(labels=index_delete)
    return df

df = pd.read_csv('house-prices.csv')
d_d = delete_row_missing_value_rate(df,50)
print(d_d.shape)