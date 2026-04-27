from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

def build_preprocessor(X_train):

    num_cols = X_train.select_dtypes(include=['int64','float64']).columns
    cat_cols = X_train.select_dtypes(include='str').columns

    numeric_transformer = Pipeline(steps=[("imputer",SimpleImputer(strategy='median'))])
    categorical_transformer = Pipeline(steps=[("imputer",SimpleImputer(strategy='most_frequent')),("onehot",OneHotEncoder(handle_unknown='ignore')) ])

    preprocessor = ColumnTransformer(transformers=[("num",numeric_transformer,num_cols),("cat",categorical_transformer,cat_cols)])

    return preprocessor