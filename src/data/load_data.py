import pandas as pd

def load_data(path:str) -> pd.DataFrame:
    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("Loaded dataset is empty")
    
    return df

