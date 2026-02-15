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

def test_no_null_prices():
    from src.data_loader import load_and_clean_data
    from src.config import OilModelConfig
    df = load_and_clean_data(OilModelConfig())
    assert df['Price'].isnull().sum() == 0

def test_data_length():
    from src.data_loader import load_and_clean_data
    from src.config import OilModelConfig
    df = load_and_clean_data(OilModelConfig())
    assert len(df) > 8000 # Historical data is large

def test_config_structure():
    from src.config import OilModelConfig
    config = OilModelConfig()
    assert hasattr(config, 'FILE_PATH')

