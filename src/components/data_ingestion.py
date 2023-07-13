import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import customException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

"""
The @dataclass decorator automatically generates special methods like '__init__', '__repr__', and '__eq__'
It simplifies the process of defining classes primarily used to hold data; reduces the amount of boilerplate code we need to write
"""

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion component")
        try:
            df = pd.read_csv('data\\stud.csv')
            logging.info('Read in data')
            """
            Extract the parent directory path using 'os.path.dirname' from 'self.ingestion_config.train_data_path'
            Then create the directory structure. 
            All the necessary intermediate directories leading up to the final directory are created
            If the parent directory or any intermediate directory does not exist, this code will create them as well
            Specifying 'exist_ok=True' prevent any errors from being raised and allow the function to proceed without making any changes if the directory already exists
            """
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train-Test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Ingestion completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise customException(e, sys)

if __name__=='__main__':
    temp = DataIngestion()
    train_data, test_data = temp.initiate_data_ingestion()

    transformer = DataTransformation()
    transformer.initiate_data_transformation(train_path=train_data, test_path=test_data)



