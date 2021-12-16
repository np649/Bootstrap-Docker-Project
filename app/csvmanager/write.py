import os
import pathlib

class Write:
    @staticmethod
    def DataFrameToCSVFile():
        path = pathlib.Path(__file__).parent / "results.csv"
        return df.to_csv(os.path.abspath(path)