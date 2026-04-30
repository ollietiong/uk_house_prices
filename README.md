# UK House Price Dynamics Analysis and Forecasting (2006-2025)

## Overview
Predicts 12-month growth in the UK House Price index using historical price and regional data.

The goal is to model medium-term housing market dynamics, relevant to mortgage risk assessment, macroeconomic and regional trend forecasting.

## Dataset
The main dataset is the ONS government dataset.
- Source - https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads-december-2025
A mapping from county (the variable 'RegionName' in the above csv) to Region is from two sources, a pdf and a csv. The pdf was manually transcribed and merged into a csv.

https://assets.publishing.service.gov.uk/media/603901d7e90e070566dafa58/Regions_and_local_authorities_at_01-04-21.pdf
https://ckan.publishing.service.gov.uk/dataset/counties-and-unitary-authorities-december-2024-boundaries-uk-bfc


## Method
### Data cleaning
The time period is restricted to avoid areas of stuctural missingness. Some counties and unitary boundaries produced conflicts based on datasets, the above UK ONS sources provided a definitive mapping that was merged with the UK HPI dataset for modelling.
### Feature Engineering
Counties and unitary boundaries are mapped to broader UK regions, and one-hot encoding is used for this categorical variable. Lag features have been built based on sales volume, growth and house price index. House price index has been normalised across the dataset.
### Modelling
The target variable is 12m growth(%) of the HPI. A random forest regressor is used as a model.
### Validation
A train-test split is performed on the last 20% of the dates, and mean absolute error is returned.
### Project Structure
├── data/
├── notebooks/
├── src/
│   ├── data/
│   │     ├──build_dataset.py
│   │     ├──clean_data.py
│   │     ├──download.py
│   │     ├──load_data.py
│   │     ├──preprocessor.py
│   │ 
│   ├── features/
│   │     ├──feature_engineering.py
│   │
│   └── models/
│   │
|   |__ pipelines/
│         ├──pipeline.py
│
├── main.py
├── README.md
├── requirements.txt

