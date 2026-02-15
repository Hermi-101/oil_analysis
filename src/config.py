from dataclasses import dataclass

@dataclass
class OilModelConfig:
    FILE_PATH: str = "data/BrentOilPrices.csv"
    TRAIN_START: str = "2019-01-01"
    TRAIN_END: str = "2021-01-01"
    TARGET_COL: str = "Price"
    DATE_COL: str = "Date"