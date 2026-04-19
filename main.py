import os
from src.data.download import download_file
from src.data.load_data import load_data


def main():
    url = "https://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/UK-HPI-full-file-2025-12.csv?utm_medium=GOV.UK&utm_source=datadownload&utm_campaign=full_fil&utm_term=9.30_18_02_26"
    path = "data/raw/UK-HPI-2025-12.csv"

    # download, load, clean pipeline
    try:
        if not os.path.exists(path): # check exists locally
            download_file(url,path)
        else:
            print(f"File exists locally, skipping download")
        df = load_data(path)
        # add clean_data function

    except FileNotFoundError as e:
        print(f"Data source missing: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error during download: {e}")
        raise


if __name__=="__main__":
    main()