import pandas as pd

def build_dataset(df):

    ''' builds a dataset into X train, y train, X test, y test 
    given a pandas dataframe. also restricts the dates to reduce 
    missing values'''

    # restrict dates
    start_date = '2007-01-01'
    end_date = '2025-11-01'

    df = df[(df['Date']>= start_date) & (df['Date'] < end_date)]

    # check no missing values
    missing = df.isna().sum()
    missing = missing[missing>0]

    if not missing.empty:
        raise ValueError(f"Missing values in dataset:\n {missing}")
    

    # split dataset into train and test
    split_idx = int(len(df)*0.8)
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]

    # split into X and y

    X_train = train.drop(columns=['12m%Change'])
    y_train = train['12m%Change']

    X_test = test.drop(columns=['12m%Change'])
    y_test = test['12m%Change']

    print("Dataset built")

    return X_train,y_train,X_test,y_test