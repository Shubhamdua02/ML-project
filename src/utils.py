import pandas as pd
import numpy as np
import dill
import os
import sys

from src.exception import customException
from src.logger import logging

def get_columns():
    try:
        df = pd.read_csv('data\\stud.csv')
        numeric_columns = []
        categorical_columns = []
        
        for column in df.columns:
            if df[column].dtype == 'O':
                categorical_columns.append(column)
            else:
                numeric_columns.append(column)
        # math score" will be our output / target variable
        numeric_columns.remove('math score')
        return (numeric_columns, categorical_columns)
    
    except Exception as e:
        raise customException(e,sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise customException(e, sys)