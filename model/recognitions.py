import base64
import json
from deepface import DeepFace as dp
import cv2

class DemographyRecognition:
    def recognize(self, base64_encoded):
        img_path = base64.b64decode(base64_encoded) # decode image
        attributes = ['age', 'gender', 'race'] # which attributes

        information = dp.analyze(img_path, attributes) # analyze

        age_json = json.loads(information) # get the age
        return (age_json) # return
