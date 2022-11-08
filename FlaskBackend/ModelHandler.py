import tensorflow as tf
import numpy as np
from PIL import Image
import io

model = None

def __load_model():
    model = tf.keras.models.load_model('PATH')

def predict(image_input_data):
  if model == None:
    __load_model()
  img = Image.open(io.BytesIO(image_input_data))
  img_arr = np.asarray(img)
  return model.predict(img_arr)
  