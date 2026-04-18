from src.data.download import download_file

def main():
    url = "https://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/UK-HPI-full-file-2025-12.csv?utm_medium=GOV.UK&utm_source=datadownload&utm_campaign=full_fil&utm_term=9.30_18_02_26"
    download_file(url,"data/raw/UK-HPI-2025-12.csv")

if __name__=="__main__":
    main()