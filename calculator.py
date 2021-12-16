"""This is the increment function"""
import pandas
import pathlib

from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class Read:
    @staticmethod
    def DataFrameFromCSVFile():
        path = pathlib.Path(__file__).parent / "results.csv"
        return pandas.read_csv(path)

class Write:
    @staticmethod
    def DataFrameToCSVFile(df: pandas.DataFrame):
        path = pathlib.Path(__file__).parent / "results.csv"
        return df.to_csv(path,float_format='%.2f', index=False, header=True)

class Calculator:
    """This is the Calculator class"""
    history = []
    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        return Calculator.history[0].getresult()
    @staticmethod
    def clear_history():
        Calculator.history.clear()
        return True
    @staticmethod
    def history_count():
        return len(Calculator.history)
    @staticmethod
    def add_calculation_to_history(calculation):
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        if Calculator.history[-1] != "NaN":
            return Calculator.history[-1].getresult()
        return Calculator.history[-1]
    @staticmethod
    def get_all_results():
        df = Read.DataFrameFromCSVFile()
        return df.values.tolist()
    @staticmethod
    def addition(value_a, value_b):
        """adds number to result"""
        addition = Addition.create(value_a,value_b)
        Calculator.add_calculation_to_history(addition)
        df = Read.DataFrameFromCSVFile()
        # new_row = 
        df.loc[len(df)] = [value_a, value_b, 'addition', addition.getresult()]
        Write.DataFrameToCSVFile(df)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def subtraction(value_a, value_b):
        """"subtract number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        df = Read.DataFrameFromCSVFile()
        df.loc[len(df)] = [value_a, value_b, 'subtraction', subtraction.getresult()]
        Write.DataFrameToCSVFile(df)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def multiplication(value_a, value_b):
        """multiplication two numbers and store the result"""
        multiplication = Multiplication.create(value_a,value_b)
        Calculator.add_calculation_to_history(multiplication)
        df = Read.DataFrameFromCSVFile()
        df.loc[len(df)] = [value_a, value_b, 'multiplication', multiplication.getresult()]
        Write.DataFrameToCSVFile(df)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def division(value_a,value_b):
        """divide two numbers and store the result"""
        if value_b != 0:
            division = Division.create(value_a,value_b)
            Calculator.add_calculation_to_history(division)
            df = Read.DataFrameFromCSVFile()
            df.loc[len(df)] = [value_a, value_b, 'division', division.getresult()]
            Write.DataFrameToCSVFile(df)
            return Calculator.get_result_of_last_calculation_added_to_history()
        else:
            Calculator.history.append("NaN")
            df = Read.DataFrameFromCSVFile()
            df.loc[len(df)] = [value_a, value_b, 'division', "NaN"]
            Write.DataFrameToCSVFile(df)
            return Calculator.get_result_of_last_calculation_added_to_history()
