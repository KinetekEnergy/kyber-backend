import json, jwt
from flask import Blueprint, app, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.titanics import predictSurvival
from model.users import User

titanic_api = Blueprint('titanic_api', __name__, url_prefix='/api/titanics')

api = Api(titanic_api)

class TitanicsAPI:
    class Passenger(Resource):
        def get(Self):
            return

   # Define the API endpoint for prediction
@app.route('/api/predict', methods=['POST'])
def predict():
    # Get the passenger data from the request
    passenger = request.get_json()

    response = predictSurvival(passenger)

    # Return the response as JSON
    return jsonify(response)