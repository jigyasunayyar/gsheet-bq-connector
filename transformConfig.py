from dataclasses import dataclass
from typing import Callable, Optional
import pandas as pd

from transformFunctions import transformlucanet


# data class to create transform config
@dataclass
class TransformConfig(dict):
    process_name: str = None,
    filepath: str = None,
    transform_func: Callable = None,
    project: str =None,
    dataset: str = None,
    table: str = None,
    chunksize: Optional[int] = 5000,
    if_exists: Optional[str] = "replace"

    @property
    def table_name(self):
        return f'{self.dataset}.{self.table}'


# example transform config
lucanet_monthly_historical = TransformConfig(
    process_name="lucanet_monthly_historical",
    filepath="/Users/j.nayyar/Downloads/LucaNet - EU - Monthly Historical.xlsx",
    project="dhh---analytics-eu",
    dataset="bl_europe_sheets",
    table="gsheet-bq-test",
    transform_func=transformlucanet,
    )

# tranform config list
transformsheets = [lucanet_monthly_historical]




