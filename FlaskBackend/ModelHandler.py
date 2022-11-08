import tensorflow as tf
import numpy as np
from PIL import Image
import io

model = None

labels = ['freshapples', 'freshbanana', 'freshoranges', 'rottenapples', 'rottenbanana', 'rottenoranges']

def __load_model():
  global model
  model = tf.keras.models.load_model('fruit_neural_network_first.h5')

def predict(image_input_data):
  print(f'image input data: {image_input_data}')
  if model == None:
    __load_model()

  img = Image.open("TestImages/rottenapple.jpg")
  print(f"IMG SIZE: {img.size}")
  img = img.resize((32,32))
  print(f"IMG SIZE 2: {img.size}")
  #img = Image.open(io.BytesIO(image_input_data))
  img_arr = np.asarray(img)
  img_arr = img_arr.reshape([-1, 32,32 ,3])
  print(f"SHAPE: {img_arr.shape}")
  result = model.predict(img_arr)
  print(f"RESULT {result}")
  label = np.argmax(result[0])
  print(labels[label])
  