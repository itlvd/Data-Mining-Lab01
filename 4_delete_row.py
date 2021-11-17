import pandas as pd

def isNan(num):
    return num!= num

def delete_row_by_list_index(l,index):
    count = 0
    for i in index:
        l.pop(i-count)
        count+=1
    return l

def delete_row_missing_value_rate(df,rate):
    head = df.columns
    #Convert pandas to list by row
    l_df = df.values.tolist()

    num_col = round(rate / 100 * len(head))
    index_delete = []
    for row in range(len(l_df)):
        count = 0
        for col in range(len(head)):
            if isNan(l_df[row][col]):
                count+=1
                if count == num_col:
                    index_delete.append(row)
                    break

    l_df = delete_row_by_list_index(l_df,index_delete)
    #Convert list to dataframe
    df = pd.DataFrame(l_df, columns=head)
    return df

df = pd.read_csv('house-prices.csv')
d_d = delete_row_missing_value_rate(df,5)
print(d_d.shape)