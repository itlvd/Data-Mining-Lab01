import pandas as pd
import sys
import getopt

def isNan(num):
    return num!= num

def is_not_Nan(num):
    return num == num

def delete_col_index(df, index):
    #matran = zip(*df)
    matran = [[df[j][i] for j in range(len(df))] for i in range(len(df[0]))]
    count = 0
    for i in index:
        matran.pop(i - count)
        count += 1

    l = [[matran[j][i] for j in range(len(matran))] for i in range(len(matran[0]))]
    return l

def delete_col_missing_value_rate(df, rate):
    head = df.columns
    head = head.tolist()
    list = df.to_numpy().tolist()

    num = round(int(rate)/100 * 1000)

    index = []
    for i in range(len(head)):  #cot
        count = 0
        for j in range(len(list)):   #dong
            if isNan(list[j][i]):
                count += 1
                if count == num:
                    index.append(i)
                    del head[i]
                    break
    list = delete_col_index(list, index)
    l = pd.DataFrame(list, columns=head)
    return l

def main():
    argv = sys.argv[1:]
    src = argv[0]  # doc ten file csv
    des = argv[1]  # doc ten file output
    expression = argv[2]

    df = pd.read_csv(src)

    df = delete_col_missing_value_rate(df, expression)
    print(df.shape)
    df.to_csv(des, sep=',', index=False)


main()
