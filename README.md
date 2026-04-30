# UK House Price Dynamics Analysis and Forecasting (2006-2025)

## Overview
This project models and forecasts 12-month growth in the UK House Price Index (HPI) using historical price and regional data.

The objective is to capture medium-term housing market dynamics relevant to:
- mortgage risk assessment  
- regional investment decisions  
- macroeconomic trend analysis  

## Why Predict 12-Month Growth?

Predicting year-on-year growth instead of raw prices:

- Reduces seasonal effects in housing data  
- Produces a more stationary target variable  

## Dataset

The primary dataset is the UK House Price Index (HPI), published by HM Land Registry.

- Monthly house price index by local authority
- Time range: 2006–2025
- Geographic granularity: county / unitary authority

Additional preprocessing:
- Local authorities were mapped to broader UK regions using official boundary data
- Source files included both CSV and PDF formats; the PDF mapping was manually transcribed and validated

## Methodology

### Data Cleaning
- Restricted time period to ensure consistent regional definitions and avoid structural missingness  
- Resolved inconsistencies between county and unitary authority boundaries using official UK datasets  
- Merged regional mapping with HPI data for modelling  

### Feature Engineering
- Target variable: 12-month percentage growth in HPI  
- Created lag features (3, 6, 12 months) for:
  - house price index  
  - transaction volume  
  - historical growth  
- Encoded regions using one-hot encoding  
- Normalised HPI values to improve model stability  

### Modelling
A Random Forest Regressor was used as a baseline non-linear model.

Rationale:
- Captures non-linear relationships between lagged features and future growth  
- Robust to feature scaling and multicollinearity  
- Provides a strong benchmark without heavy tuning  

### Validation
- Time-based train-test split (last 20% of observations used as test set)  
- Evaluation metric: Mean Absolute Error (MAE)  

This approach preserves temporal ordering and avoids look-ahead bias.

## Results

The Random Forest model achieved:

- MAE: 0.67 percentage points on 12-month growth

Key observations:
- Lagged growth features were the most predictive  
- Regional effects contributed but were secondary to temporal dynamics  

### Project Structure
```bash
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
```
