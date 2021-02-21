from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import numpy as np
import pandas, joblib

APP = Flask(__name__)
API = Api(APP)

#Load machine learning model
MODEL = joblib.load('recommend_model.pkl')

#Print out prediction value
class Predict(Resource):
    def post(self):
        #Gain access to variables on the flask.request object
        parser = reqparse.RequestParser()
        #Bring 'rest_name' and 'rest_category' values for ML run
        parser.add_argument('rest_name')
        parser.add_argument('rest_category')
        args = parser.parse_args()  
        print('###args###')
        _rest_name = args['rest_name']
        _rest_category = args['rest_category']
        print(args)
        #Insert the values into the model
        prediction = MODEL(_rest_name, _rest_category)
        #Change the format of the recommendation list
        listt = []
        for i in range(len(prediction)):
          listt.append(prediction.iloc[i].to_dict())
        #Return the recommendation list in json format
        return jsonify(listt)
    def get(self):
      return 'try again', 200

#Add a resource to the api
API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=True, port='1080')