import pytest
import pandas as pd
from src.data_loader import load_and_clean_data
from src.config import OilModelConfig

def test_data_columns():
    config = OilModelConfig()
    # Mock some data or load real data
    df = load_and_clean_data(config)
    assert "Price" in df.columns

def test_date_index():
    config = OilModelConfig()
    df = load_and_clean_data(config)
    assert isinstance(df.index, pd.DatetimeIndex)

