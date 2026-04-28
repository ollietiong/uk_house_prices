import pandas as pd

def clean_data(df:pd.DataFrame,regions:pd.DataFrame)-> pd.DataFrame:

    # create copy
    df = df.copy()

    # drop variables not required
    df = df[['Date','RegionName','AreaCode','AveragePrice','Index','1m%Change','12m%Change','SalesVolume']]

    # check no duplicates - TO BE REFACTORED
    assert df.duplicated().sum()==0

    # convert date column to datetime
    df['Date'] = pd.to_datetime(df['Date'].astype(str).str.strip(),format='%d/%m/%Y',errors='raise')

    # restrict data to avoid missing values
    #end_date = '2025-11-01' # non inclusive
    #start_date = '2004' # inclusive

    #df = df[(df['Date']>= start_date) & (df['Date'] < end_date)]

    # merge to regions
    # rename column in regions to merge on
    #regions = regions.rename(columns={"County": "RegionName"})
    df = df.merge(regions, on='RegionName',how='left')


    return df

