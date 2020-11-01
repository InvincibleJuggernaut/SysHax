from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
import cv2

from main import *

def predict_side_mirror(img_path):
    # Loading the model
    json_file = open("Models/Mirror_Model.json", "r")
    model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(model_json)
    # load weights into new model
    loaded_model.load_weights("Models/Mirror_Model.h5")
    print("Loaded model from disk")

    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    pred = loaded_model.predict(img_tensor)
    if pred[0][0] > pred[0][1]:
        return "Damaged"
    else:
        return "Undamaged"
    print(result)

# def predict_headlights(image_path):
#   # Loading the model
#   json_file = open("/content/drive/My Drive/GOVT_HACK/Models/Headlights_Model.json", "r")
#   model_json = json_file.read()
#   json_file.close()
#   loaded_model = model_from_json(model_json)
#   # load weights into new model
#   loaded_model.load_weights("/content/drive/My Drive/GOVT_HACK/Models/Headlights_Model.h5")
#   print("Loaded model from disk")

#   img = image.load_img(img_path, target_size=(224, 224))
#   img_tensor = image.img_to_array(img)
#   img_tensor = np.expand_dims(img_tensor, axis=0)
#   img_tensor /= 255.

#   pred = loaded_model.predict(img_tensor)

#   if pred[0][0]>pred[0][1]:
#     return "damaged"
#   else:
#     return "undamaged"


def predict_windscreen(img_path):
    # Loading the model
    json_file = open("Models/Windscreen_Model.json", "r")
    model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(model_json)
    # load weights into new model
    loaded_model.load_weights("Models/Windscreen_Model.h5")
    print("Loaded model from disk")

    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    pred = loaded_model.predict(img_tensor)

    if pred[0][0] > pred[0][1]:
        return "Damaged"
    else:
        return "Undamaged"


def predict_damage(img_path):
    # Loading the model
    json_file = open("Models/Damage_or_Undamaged_Model.json", "r")
    model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(model_json)
    # load weights into new model
    loaded_model.load_weights("Models/Damage_or_Undamaged_Model.h5")
    print("Loaded model from disk")

    img = image.load_img(img_path, target_size=(224, 224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    pred = loaded_model.predict(img_tensor)
    print(pred)
    if pred[0][0] > pred[0][1]:
        return "Damaged"
    else:
        return "Undamaged"


def generate_result():
    return result

#x=predict_windscreen("Testing/k.jpg")
#y=predict_side_mirror("Testing/c.jpg")

#print(x)
#print(y)
