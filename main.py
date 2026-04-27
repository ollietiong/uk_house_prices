import os
from sklearn.pipeline import Pipeline
from src.data.download import download_file
from src.data.load_data import load_data
from src.data.clean_data import clean_data
from src.data.preprocessor import build_preprocessor
from src.data.build_dataset import build_dataset
from src.features.feature_engineering import FeatureEngineer



def main():
    url = "https://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/UK-HPI-full-file-2025-12.csv?utm_medium=GOV.UK&utm_source=datadownload&utm_campaign=full_fil&utm_term=9.30_18_02_26"
    path_main = "data/raw/UK-HPI-2025-12.csv"
    path_regions = "data/uk-counties-to-regions.csv"

    # download, load, clean pipeline
    try:
        # download data if required
        if not os.path.exists(path_main): # check exists locally
            download_file(url,path_main)
        else:
            print(f"File exists locally, skipping download")
        # load data
        df = load_data(path_main)
        regions = load_data(path_regions)
        df = clean_data(df,regions)

        #foo = FeatureEngineer()
        #df = foo.fit_transform(df)

        X_train,y_train, X_test,y_test = build_dataset(df)

        # build components
        preprocessor = build_preprocessor(X_train)
        # model = build_model()

        # pipeline for model
        pipeline = Pipeline(steps=[("features",FeatureEngineer()),("preprocessor",preprocessor),("model",model)])

        
    except FileNotFoundError as e:
        print(f"Data source missing: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error during download: {e}")
        raise


if __name__=="__main__":
    main()