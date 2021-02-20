import numpy as np
from keras.preprocessing import image
from keras.layers import *
from keras.models import Model, load_model
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint
import pickle

# loading the model
model = load_model("./storage/BEST_MODEL.h5")

# Loading the dictionary
with open("./storage/idx2pok.pkl", "rb") as f:
    idx2pok = pickle.load(f)

def preprocess_img(img_path):

    img = image.load_img(img_path, target_size=(400, 400))
    img = image.img_to_array(img)
    # reshaping the image
    img = np.expand_dims(img, axis=0)
    # Normalizing pixlels from [0.0, 255.0] to [-1.0, 1.0]
    img = img.astype(np.float32) / 255.0
    img = (img - 0.5) * 2

    return img

def predict_pokemon(photo):

    pred = idx2pok[np.argmax(model.predict(photo))]
    return pred

def pokeDex(img_path):

    img = preprocess_img(img_path)
    pred_pokemon = predict_pokemon(img)
    return pred_pokemon