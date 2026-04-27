import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self,X):

        X = X.sort_values('Date').copy()

        
        # GROUPED FEATURES
        grp = X.groupby('RegionName')

        # normalise index
        X['norm_index'] = grp['Index'].transform(lambda x:x/x.iloc[0]*100)
        # create rolling features
        X['YoYRolling3'] = grp['12m%Change'].rolling(3).mean().reset_index(level=0, drop=True)
        X['IndexRolling12'] = grp['norm_index'].rolling(12).mean().reset_index(level=0, drop=True)
        X['YoYRollingStd6'] = grp['12m%Change'].rolling(6).std().reset_index(level=0, drop=True)

        # create lag features on growth
        X['lag1_12mGrowth'] = grp['12m%Change'].shift(1)
        X['lag3_12mGrowth'] = grp['12m%Change'].shift(3)
        X['lag12_12mGrowth'] = grp['12m%Change'].shift(12)

        # create lag features on sales volume
        X["lag_1_sales_vol"] = grp["SalesVolume"].shift(1)
        X["lag_6_sales_vol"] = grp["SalesVolume"].shift(6)
        X["6mChange_sales_vol"] = grp["SalesVolume"].pct_change(6)

        X = X.drop(columns=['RegionName','AreaCode','AveragePrice','Index'])

        return X
    

    '''
    def restrict_date_range(df:pd.DataFrame)->pd.DataFrame: 
        start_date = '2007-01-01'
        end_date = '2025-11-01'

        df = df[(df['Date']>= start_date) & (df['Date'] < end_date)]
        return df'''