import tensorflow as tf
import numpy as np
from PIL import Image
import io

model = None
model_path = 'Models/fruit_neural_network_v5.h5'
labels = ['freshapples', 'freshbanana', 'freshoranges', 'rottenapples', 'rottenbanana', 'rottenoranges']

def __load_model():
  global model
  model = tf.keras.models.load_model(model_path)

def __load_image(image_data):
  print(image_data)
  return Image.open(io.BytesIO(image_data))

def __format_image(img):
  img = img.resize((32,32))
  print(f"IMG SIZE AFTER RESIZE: {img.size}")
  img_arr = np.asarray(img)
  return img_arr.reshape([-1, 32, 32, 3])

def predict(image_input_data):
  if model == None:
    __load_model()
  img = __load_image(image_input_data)
  print(f"IMG SIZE BEFORE RESIZE: {img.size}")
  img_arr = __format_image(img)
  print(f"SHAPE: {img_arr.shape}")
  result = model.predict(img_arr)
  print(f"RESULT: {result}")
  label = np.argmax(result[0])
  print(f"FINAL LABEL RESULT: {labels[label]}")
  return labels[label]
  