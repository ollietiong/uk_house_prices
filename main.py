import os
from sklearn.pipeline import Pipeline
from src.data.download import download_file
from src.data.load_data import load_data
from src.data.clean_data import clean_data
from src.data.preprocessor import build_preprocessor
from src.data.build_dataset import build_dataset
from src.features.feature_engineering import FeatureEngineer
from src.pipelines.pipeline import build_pipeline
from sklearn.metrics import mean_absolute_error


def main():

    ''' Main entry point for UK House Price forecasting project.

    This script orchestrates the end-to-end pipeline, including:
    - Loading raw data
    - Preprocessing and feature engineering
    - Training the model
    - Evaluating performance
    - Saving trained artifacts

    Usage:
        python main.py
    
    Inputs:
        - Raw datasets (main house price data - data/raw/UK-HPI-2025-12.csv, region mapping - data/full_counties_to_regions.csv)
    
    Outputs:
        - Evaluation metrics printed
    '''


    url = "https://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/UK-HPI-full-file-2025-12.csv?utm_medium=GOV.UK&utm_source=datadownload&utm_campaign=full_fil&utm_term=9.30_18_02_26"
    path_main = "data/raw/UK-HPI-2025-12.csv"
    path_regions = "data/full_counties_to_regions.csv"

    
    try:
        # download data if required
        if not os.path.exists(path_main): # check exists locally
            download_file(url,path_main)
        else:
            print(f"File exists locally, skipping download")

        # load data
        df = load_data(path_main)
        regions = load_data(path_regions)

        # clean data
        df = clean_data(df,regions)

        # build time lag features
        features = FeatureEngineer()
        df = features.transform_time_features(df)

        # build dataset
        X_train, y_train, X_test,y_test = build_dataset(df)

        # Build pipeline
        pipe = build_pipeline(X_train)

        # Train model
        pipe.fit(X_train,y_train)
        print("Model fit to training data")

        # Evaluate
        preds = pipe.predict(X_test)
        mae = mean_absolute_error(y_test, preds)

        print(f"Mean absolute error: {mae}")

        
    except FileNotFoundError as e:
        print(f"Data source missing: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error during download: {e}")
        raise


if __name__=="__main__":
    main()