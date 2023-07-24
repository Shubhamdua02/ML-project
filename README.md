<h1 align="center">
  End-to-End ML Project
  
 [![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
</h1>

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](https://opensource.org/license/mit/)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/shubhamdua02/ML-project)](https://img.shields.io/github/repo-size/shubhamdua02/ML-project)
[![made-with-python](https://img.shields.io/badge/Made_with-Python-blue)](https://www.python.org/)
[![Python 3.8](https://img.shields.io/badge/Python-3.8-blue)](https://www.python.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/shubhamdua02/ML-project)](https://github.com/shubhamdua02/ML-project/graphs/contributors)
[![Open Issues](https://img.shields.io/github/issues/shubhamdua02/ML-project)](https://github.com/shubhamdua02/ML-project/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/shubhamdua02/ML-project)](https://github.com/shubhamdua02/ML-project/pulls)

</div>

## Life Cycle of Machine Learning Project
* Understanding the Problem Statement
* Data Collection
* Data Checks to perform
* Exploratory data analysis
* Data Pre-Processing
* Model Training
* Choose the best model

## Problem Statement
This project understands how the student's performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course.

## Data Collection 
The [dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams) is publically available on Kaggle and consists of 8 columns and 1000 rows.

## Installation Procedure
- Create a virtual environment (this step is optional)
- Install Python 3.8 or higher (This project was run with Python 3.8)
- Clone the repository:
```
https://github.com/Shubhamdua02/ML-project.git
```
- Install the necessary packages and libraries
```
pip install -r requirements.txt  
```
- Run data_ingestion.py present inside src\components;
  This will overwrite the data files and pickle files present inside the [artifacts](https://github.com/Shubhamdua02/ML-project/tree/main/artifacts) folder
```
cd ML-project
python src\components\data_ingestion.py
```
- Run app.py
```
python app.py
```
- Go to your web browser and type in http://127.0.0.1:5000/predict_data
- Fill up the input fields, and get the predicted Math Score
