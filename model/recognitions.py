import base64
import json
from deepface import DeepFace as dp
import cv2

class DemographyRecognition:
    def recognize(self, base64_encoded):
        parsed = base64_encoded["base64_encoded"]  # remove from dictionary
        # print(parsed)
        img_path = base64.b64decode(parsed)  # decode image
        attributes = ['age', 'gender', 'race'] # which attributes

        information = dp.analyze(img_path, attributes) # analyze

        age_json = json.loads(information) # get the age
        return (age_json) # return
