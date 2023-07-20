import sys
import pandas as pd
from src.exception import customException
from src.logger import logging
from src.utils import load_object
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        """
        features: dataframe of input features by user, results in prediction for user input
        """
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            scaled_data=preprocessor.transform(features)
            predictions=model.predict(scaled_data)
            return predictions
        
        except Exception as e:
            raise customException(e,sys)

class CustomData:
    """
    takes input features from an HTML form (POST METHOD) and returns a dataframe to feed into the model
    """
    def __init__(self, 
                 gender:str,
                 race_ethnicity:str,
                 parental_level_of_education:str,
                 lunch:str,
                 test_preparation_course:str,
                 reading_score:int,
                 writing_score:int):
        
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
    
    def asDataFrame(self):
        try:
            data_dictionary = {
                'gender':[self.gender],
                'race_ethnicity':[self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            return pd.DataFrame(data_dictionary)
        
        except Exception as e:
            raise customException(e,sys)