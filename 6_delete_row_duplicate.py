import pandas as pd
import sys

def isNan(num):
    return num!= num

def delete_row_duplicate(df):
    head = df.columns
    l_df = df.to_numpy().tolist()
    row = len(l_df)
    col = len(l_df[0])
    i = 0
    while (i < row):
        A = []
        for j in range(col):
            A.append(l_df[i][j])
        # A.to_numpy().tolist()
        r = i + 1
        while (r < row):
            B = []
            for c in range(col):
                B.append(l_df[r][c])
            # B.to_numpy().tolist()
            if A == B:
                l_df.pop(r)
                row -= 1
            else:
                r += 1
        i += 1

    l_df = pd.DataFrame(l_df, columns=head)
    return l_df

def main():
    argv = sys.argv[1:]
    src = argv[0]  # doc ten file csv
    des = argv[1]  # doc ten file output

    df = pd.read_csv(src)
    df = delete_row_duplicate(df)
    print(df.shape)

    df.to_csv(des, sep = ',', index = False)


main()