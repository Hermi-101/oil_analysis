import pandas as pd
from typing import Tuple
from src.config import OilModelConfig

def load_and_clean_data(config: OilModelConfig) -> pd.DataFrame:
    """Loads and cleans the dataset with strict date parsing."""
    df = pd.read_csv(config.FILE_PATH)
    # Handling mixed formats found in Week 11
    df[config.DATE_COL] = pd.to_datetime(df[config.DATE_COL], format='mixed')
    df = df.set_index(config.DATE_COL).sort_index()
    return df