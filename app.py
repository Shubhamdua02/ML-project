from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from sklearn.preprocessing import StandardScaler
from src.logger import logging

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_data', methods=['GET','POST'])
def prediction():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=request.form.get('reading_score'),
            writing_score=request.form.get('writing_score')
        )

        data_df=data.asDataFrame()
        print(data_df)

        prediction_pipeline = PredictPipeline()
        results = prediction_pipeline.predict(data_df)
        return render_template('home.html', results=results)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)