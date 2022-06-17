from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import  load_img
import tensorflow as tf
from PIL import Image
img_data = np.random.random(size=(100, 100, 3))
img = tf.keras.preprocessing.image.array_to_img(img_data)
array = tf.keras.preprocessing.image.img_to_array(img)
import numpy as np
import streamlit as st
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import os.path


@st.cache(allow_output_mutation=True)
def get_model():
        model = load_model('/Users/ads-14/Desktop/traffic/traffic_Data/Traffic_Sign_Classifier_CNN.hdf5')
        print('Model Loaded')
        return model 

        
def predict(image):
        loaded_model = get_model()
        image = load_img(image, target_size=(32, 32), color_mode = "grayscale")
        image = img_to_array(image)
        image = image/255.0
        image = np.reshape(image,[1,32,32,1])

        classes = np.argmax(loaded_model.predict(image))

        return classes
       