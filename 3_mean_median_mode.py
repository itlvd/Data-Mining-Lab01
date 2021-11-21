import pandas as pd
import sys

def is_not_Nan(num):  #tra ve true neu no nan
    return num == num

def isNan(num):
    return num != num

def dtype(l):
    for i in l:
        if(isNan(i)):
            continue
        else:
            return type(i)

def get_mean(df, attribute):
    data = df[attribute].values.tolist()
    count = 0
    sum = 0
    for i in data:
        if is_not_Nan(i):
            sum += i
            count += 1
    return sum/count

def get_median(df, attribute):
    data = df[attribute].to_numpy().tolist()
    Array = []
    for i in data:
        if is_not_Nan(i):
            Array.append(i)
    Array.sort()
    if len(Array)%2 == 1:
        return Array[len(Array)//2]
    else:
        return (Array[len(Array)//2] + Array[len(Array)//2 + 1])/2

def get_mode(df, attribute):
    data = df[attribute].to_numpy().tolist()
    dmax = -99

    for i in range(len(data)):
        if data.count(data[i]) > dmax and is_not_Nan(data[i]):
            dmax = data.count(data[i])
            x = data[i]
    return x


def main():
    argv = sys.argv[1:]
    src = argv[0]  #doc ten file csv
    des = argv[1]  #doc ten file output
    expression = argv[2]
    type = argv[3]

    df = pd.read_csv(src)


    columns = expression.split(',')
    if any(x not in df.columns for x in columns):
        print('Columns is not exist. Please check again!')
        return
    print(columns)

    if type == 'mean':
        for col in columns:
            data = df[col].to_numpy().tolist()

            if (dtype(data) is str):
                print('Your column is not numeric. Please check again!: ', col)
                break

            res = get_mean(df, col)   #tim so trung binh cong
            for i in range(len(data)):
                if isNan(data[i]):    #gan so res vao vi tri rong
                    data[i] = res

            df[col] = data
            df.to_csv(des, sep=',', index=False)
    elif type == 'median':
        for col in columns:
            data = df[col].to_numpy().tolist()

            if (dtype(data) is str):
                print('Your column is not numeric. Please check again!: ', col)
                break

            res = get_median(df, col)
            for i in range(len(data)):
                if isNan(data[i]):
                    data[i] = res
            df[col] = data
            df.to_csv(des,sep=',',index=False)
    else:
        for col in columns:
            data = df[col].to_numpy().tolist()

            if (dtype(data) is int):
                print('Your column is numeric. Please check again!: ', col)
                break

            res = get_mode(df, col)
            for i in range(len(data)):
                if isNan(data[i]):
                    data[i] = res
            df[col] = data
            df.to_csv(des, sep=',', index=False)


main()
