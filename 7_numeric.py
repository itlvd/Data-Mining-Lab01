import pandas as pd
import sys
import getopt
import math

def isNan(num):
    return num!= num

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

    if columns == 'all':
        columns = df.columns
    else:
        columns = columns.split(',')
        if any(x not in df.columns for x in columns):
            print('Columns is not exist. Please check again!')
            return

    for col in columns:
        #Check columns is a numberic
        if(df[col].dtype in ['O','S','U','V']) or col == 'Id':
            continue

        #Convert type to float.
        df[col] = df[col].astype(float)
        if(mode == 'min-max'):
            df[col] = min_max(df[col])
        else:
            df[col] = z_score(df[col])
    
    df.to_csv(des,sep=',',index=False)

main()