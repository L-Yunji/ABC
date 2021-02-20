from flask import Flask, jsonify, render_template, request
#from flask_restful import Api, Resource, reqparse
#import numpy as np
#import joblib
import pandas as pd

APP = Flask(__name__)
#API = Api(APP)

#Load machine learning model
MODEL = joblib.load('recommend_model.pkl')

@APP.route('/')
def home():
  return render_template('index.html')

#Print out prediction value
class Predict(Resource):
    #@staticmethod
    #Set HTTP routes
    @APP.route('/predict', methods=['POST', 'GET'])
    def predict():
        rest_df = pd.read_csv('data_0211.csv')
        inp1 = request.form["Restaurant_Name"]
        inp2 = request.form["Recommendation_Category"]
        prediction = MODEL(inp1, inp2)
        return render_template('index.html', tables=[prediction.to_html(classes='data', header="true")], titles=rest_df.columns) 
##API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=True, port='1080')
