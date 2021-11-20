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
    df[expression] = ret
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
        print("Something went wrong. Please notify me :)")

    df.to_csv(des,sep=',',index=False)

main()
