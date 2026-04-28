from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

from src.data.preprocessor import build_preprocessor
from src.features.feature_engineering import FeatureEngineer


def build_pipeline(X_train):

    # build components
    preprocessor = build_preprocessor(X_train)
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    
    # pipeline for model
    pipe = Pipeline(steps=[("features",FeatureEngineer()),("preprocessor",preprocessor),("model",model)])

    return pipe