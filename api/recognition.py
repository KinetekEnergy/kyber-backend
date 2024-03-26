from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource  # used for REST API building

from model.recognitions import DemographyRecognition

recognition_api = Blueprint("recognition_api", __name__, url_prefix="/api/recognition")

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(recognition_api)

class RecognitionApi:
    class _CRUD(Resource):
        def post(self):
            data = request.get_json()
            demography = DemographyRecognition.recognize(self, base64_encoded=data)
            return jsonify(demography)
    api.add_resource(_CRUD, "/")
