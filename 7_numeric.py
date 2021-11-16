import pandas as pd
import sys
import getopt

def min_max(series_col_df):
    #Convert NaN to zero
    for i in range(len(series_col_df)):
        series_col_df[i] = 0 if (pd.isnull(series_col_df[i])) else series_col_df[i]

    return (series_col_df - min(series_col_df)) / ((max(series_col_df) - min(series_col_df)) if (max(series_col_df) - min(series_col_df)) > 0 else len(series_col_df))

def z_score(series_col_df):
    #Convert NaN to zero
    for i in range(len(series_col_df)):
        series_col_df[i] = 0 if (pd.isnull(series_col_df[i])) else series_col_df[i]

    mean = sum(series_col_df) / len(series_col_df)
    std_devition = (sum(abs(series_col_df-mean)**2)/len(series_col_df))**(1/2)
    return (series_col_df - mean)/std_devition

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
        -c, --columns: Yours input. Seperate by comma.
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
        columns = [df.columns]
    else:
        columns = columns.split(',')
        if any(x not in df.columns for x in columns):
            print('Columns is not exist. Please check again!')
            return

    for col in columns:
        #Check columns is a numberic
        if(df.iloc[:,col].dtype in ['O','S','U','V']):
            continue

        #Convert type to float.
        df.iloc[:,col] = df.iloc[:,col].astype(float)
        if(mode == 'min-max'):
            df.iloc[:,col] = min_max(df.iloc[:,col])
        else:
            df.iloc[:,col] = z_score(df.iloc[:,col])
    
    df.to_csv(des,sep=',')

main()