import os
import sys
import json

from dataclasses import dataclass
from src.exception import customException
from src.logger import logging
from src.utils import save_object, evaluate_model, save_model_score

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.metrics import r2_score

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join("artifacts", "model.pkl")
    model_score_path = os.path.join("models", "score_report.json")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('Initiate Model Training')
            
            x_train, y_train, x_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            logging.info(f"x_train size: {x_train.shape}, x_test size: {x_test.shape}, y_train size: {y_train.shape}, y_test size: {y_test.shape}")

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            # model_report is a dictionary that will return the names and R2 scores of all the models
            model_report = {}
            model_report = evaluate_model(x_train, x_test, y_train, y_test, models=models)
            logging.info('Models trained')
            
            save_model_score(
                model_score=model_report,
                file_path=self.model_trainer_config.model_score_path
            )
            logging.info('Model scores saved')

            # best_model is a tuple that will return the name of the best model and the R2 score
            best_model = max(model_report.items(), key=lambda item:item[1])

            logging.info(f"The best model is {best_model[0]} with an R2 score of {best_model[1]}")

            # best_model_obj is an intance of the model class with the highest R2 score
            best_model_obj = models[best_model[0]]

            save_object(
                file_path=self.model_trainer_config.trained_model_path,
                obj=best_model_obj
            )

            logging.info('Model saved as pickle file')

            # these lines are redundant because we also get the R2 score from src.utils.evaluate_model
            y_pred = best_model_obj.predict(x_test)
            R2score = r2_score(y_test, y_pred)
            return R2score

        except Exception as e:
            raise customException(e, sys)