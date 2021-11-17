import pandas as pd
import sys
import getopt
import math
import copy

def isNan(num):
    return num!= num

def dtype(l):
    for i in l:
        if(isNan(i)):
            continue
        else:
            return type(i)

def min_max(l_col):
    #Convert NaN to zero
    for i in range(len(l_col)):
        l_col[i] = 0 if (isNan(l_col[i])) else l_col[i]
    return [((x - min(l_col)) / ((max(l_col) - min(l_col)) if (max(l_col) - min(l_col)) > 0 else len(l_col))) for x in l_col]

def z_score(l_col):
    #Convert NaN to zero
    for i in range(len(l_col)):
        l_col[i] = 0 if (isNan(l_col[i])) else l_col[i]

    mean = sum(l_col) / len(l_col)
    std_devition = math.sqrt(sum([(abs(x-mean)**2) for x in l_col])/len(l_col))
    return [((x - mean)/std_devition) for x in l_col]

def main():
    src = None
    des = 'output.csv'
    mode = 'min-max'
    columns = 'all'
    merge_col = []
    head = None

    argv = sys.argv[1:]

    if argv[0] in ['-h','--help']:
        print('''
        -s, --source: Yours file csv to normalization.
        -d, --destination: Output the result.
        -m, --mode: This file have 2 options (min-max, z-score). Input the name of normaliztion that you choose.
        -c, --columns: Yours columns. Seperate by comma.
        -h, --help: If you have any problem. You can find a solution here.
        ''')
        return

    try:
        opts, args = getopt.getopt(argv, "s:d:c:m:", ["source=","destination=","columns=","mode="])
    except:
        print("Error! Please try: --source, --destination, --mode, --columns(name of column or \"--columns=all\" for all columns)")


    for opt, arg in opts:
        if opt in ['-s', '--source']:
            src = arg
        elif opt in ['-d', '--destination']:
            des = arg
        elif opt in ['-m','--mode']:
            mode = arg
        elif opt in ['-c','--columns']:
            columns = arg
            

    df = pd.read_csv(src)
    head = df.columns

    if columns == 'all':
        columns = df.columns
    else:
        columns = columns.split(',')
        if any(x not in df.columns for x in columns):
            print('Columns is not exist. Please check again!')
            return

    
    for col in columns:
        #Convert columns dataframe to list
        l_col = df[col].values.tolist()
        
        #Check columns is a numberic
        if (dtype(l_col) is str) or col == 'Id':
            merge_col.append(l_col)
            continue

        if(mode == 'min-max'):
            l_col = min_max(l_col)
        else:
            l_col = z_score(l_col)
        
        merge_col.append(l_col)

    df =pd.DataFrame(merge_col).T
    df.columns = head
    df.to_csv(des,sep=',',index=False)

main()