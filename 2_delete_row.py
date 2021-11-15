import pandas as pd
import sys

def count_row_miss_value(df):
    count = 0
    for row in range(df.shape[0]):
        for col in range(df.shape[1]):
            if pd.isnull(df.iat[row,col]):
                count +=1
                break
    return count

def main():
    argv = sys.argv[1]
    src = argv

    df = pd.read_csv(src)
    print(count_row_miss_value(df))

main()