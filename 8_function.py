import pandas as pd
import sys

def cal(df,expression):
    head = df.columns
    ret = []
    for i in range(df.shape[0]):
        dictx={}
        for j in head:
            s = df[j].values.tolist()
            dictx[j]=s[i]
        ret.append(eval(expression,dictx))
    df['result'] = ret
    return df

def main():
    src = None
    des = None
    expression = ""

    argv = sys.argv[1:]
    src = argv[0]
    des = argv[1]
    expression = argv[2]

    df = pd.read_csv(src)

    try:
        df = cal(df,expression)
    except:
        print("Value of your columns is not numberic Please check again")

    df.to_csv(des,sep=',',index=False)

main()
