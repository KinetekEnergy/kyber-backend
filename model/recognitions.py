import base64
import io
import json
from deepface import DeepFace as dp
from PIL import Image
import cv2
import numpy as np


class DemographyRecognition:
    def recognize(self, base64_encoded):
        # image parsing in preparation
        b64_string = base64_encoded["base64_encoded"]  # remove from dictionary

        if b64_string.startswith("data:image"):  # if headers --> remove
            b64_string = b64_string.split(",", 1)[1]

        image_data = base64.b64decode(b64_string)  # decoding

        image = Image.open(io.BytesIO(image_data))  # get the image

        image_np = np.array(image)  # convert to np array

        # analysis
        attributes = ["age", "gender"]  # which attributes
        information = dp.analyze(image_np, attributes)  # analyze

        data = information[0] # get the first element
        age = data['age'] # age extraction

        bothGenders = data['gender'] # get both gender confidence rates
        woman = bothGenders['Woman'] # woman confidence
        man = bothGenders['Man'] # man confidence
        gender = max(woman, man) # find the greater one
        
        print(age)
        print(gender)

        return age  # return

    def parseImage():
        pass
