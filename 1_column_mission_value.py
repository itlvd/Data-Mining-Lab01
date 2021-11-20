import pandas as pd
import sys

def isNan(num):
    return num != num

def count_column_miss_value(df):
    head = df.columns
    count = []

    for i in range(1, 81):  #cot
        for j in range(df.shape[0]):  #dong
            if isNan(df.iat[i,j]):
                count.append(head[i])
                break
    return count

def main():
    argv = sys.argv[1]
    src = argv

    df = pd.read_csv(src)
    print(count_column_miss_value(df))

main()