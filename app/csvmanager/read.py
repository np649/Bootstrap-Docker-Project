import os
import pathlib

import pandas as pd

class Read:
    @staticmethod
    def DataFrameFromCSVFile():
        path = pathlib.Path(__file__).parent / "result.csv"
        return pd.read_csv(path)