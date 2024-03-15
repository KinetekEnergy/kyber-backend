import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource
from datetime import datetime

from model.titanics import TitanicRegression, predictSurvival

# Define the Titanic API blueprint
titanic_api = Blueprint("titanic_api", __name__, url_prefix="/api/titanic")
api = Api(titanic_api)


class TitanicAPI:
    class Passenger(Resource):
        def get(self):
            passenger = request.get_json()
            response = predictSurvival(passenger)
            return jsonify(response)

    api.add_resource(Passenger, "/")  # Register Passenger resource