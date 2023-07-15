import pandas as pd
import numpy as np
import dill
import os
import sys
import json
from sklearn.metrics import r2_score

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

def save_model_score(model_score:dict, file_path):
    """
    model_score : a dictionary with model names and their respective metric scores
    file_path : the path where the json file is dumped
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'w') as file_obj:
            json.dump(model_score, file_obj)
    
    except Exception as e:
        pass
    
def evaluate_model(x_train, x_test, y_train, y_test, models:dict):
    """
    x_train : training dataset with list of input features
    x_test : training dataset with target variable(s)
    y_train : test dataset with list of input features
    y_test : test dataset with target variable(s)
    models : list of models to evaluate, in the form of a dictionary (key: name of model, value: the model)
    """
    try:
        report = {}
        for model_name,model in models.items():
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            model_score = r2_score(y_test, y_pred)
            report[model_name] = model_score
        return report

    except Exception as e:
        raise customException(e,sys)