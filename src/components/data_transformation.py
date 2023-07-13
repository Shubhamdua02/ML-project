import sys
import os
import numpy as np
import pandas as pd
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# from src.components.data_ingestion import DataIngestion
from src.utils import get_columns, save_object
from src.exception import customException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()
    
    def transform_data_obj(self):
        """
        This function is repsonsible for data transformation
        """
        try:
            numeric_columns, categorical_columns = get_columns()

            numeric_pipeline = Pipeline(
                steps = [("imputer", SimpleImputer(strategy='median')),
                        ("scaler", StandardScaler())]
            )
            categorical_pipeline = Pipeline(
                steps = [("imputer", SimpleImputer(strategy='most_frequent')),
                        ("encoder", OneHotEncoder())]
            )

            logging.info(f'Numerical columns : {numeric_columns}')
            logging.info(f'Categorical columns : {categorical_columns}')

            preprocessor = ColumnTransformer(
                [('Numeric_pipeline', numeric_pipeline, numeric_columns),
                ('Categorical_pipeline', categorical_pipeline, categorical_columns)]
            )

            return preprocessor
        
        except Exception as e:
            raise customException(e,sys)
        

    def initiate_data_transformation(self, train_path, test_path):
        try:
            df_train = pd.read_csv(train_path)
            df_test = pd.read_csv(test_path)

            logging.info('Read in Train and Test data')

            preprocesor_obj = self.transform_data_obj()

            target_column = "math score"
            numeric_columns,_ = get_columns()

            x_train = df_train.drop(columns=[target_column], axis=1)
            y_train = df_train[target_column]
            x_test = df_test.drop(columns=[target_column], axis=1)
            y_test = df_test[target_column]

            logging.info('Apply preprocessing on train and test data')

            x_train_preprocess = preprocesor_obj.fit_transform(x_train)
            x_test_preprocess = preprocesor_obj.transform(x_test)

            train_arr = np.c_[x_train_preprocess, np.array(y_train)]
            test_arr = np.c_[x_test_preprocess, np.array(y_test)]

            save_object(
                file_path=self.transformation_config.preprocessor_file_path,
                obj = preprocesor_obj
            )
            logging.info('Object saved as pickle file')
            return(
                train_arr, test_arr, self.transformation_config.preprocessor_file_path
            )

        
        except Exception as e:
            raise customException(e, sys)