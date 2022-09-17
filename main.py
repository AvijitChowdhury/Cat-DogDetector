import os

import cv2
import keras
import numpy as np
import pandas as pd
import streamlit as st
from keras.applications.imagenet_utils import (decode_predictions,
                                               preprocess_input)
from PIL import Image
from tensorflow.keras.layers import (BatchNormalization, Conv2D, Dense,
                                     Dropout, Flatten, MaxPooling2D)
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing import image

COUNT =0


def load_image(path):
    # global COUNT
    img = image.load_img(path,target_size=model.input_shape[1:3]) 
    x = image.img_to_array(img) 
    x = np.expand_dims(x,axis=0) 
    x = preprocess_input(x) 
    # COUNT=COUNT-1
    return img,x

model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(128,128,3)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
model.load_weights('static/model.h5')




st.title('Dog and Cat Image Classifier')
image_file = st.file_uploader("Upload Image",type=["csv","png","jpg","jpeg"])
if image_file is not None:
    
    file_details = {"FileName":image_file.name,"FileType":image_file.type}
    st.write(file_details)
    img = load_image(image_file)
    #st.image(img,height=250,width=250)
    temp=str(COUNT)
    try:
        with open(os.path.join("tempDir",temp),"wb") as f: 
            f.write(image_file.getbuffer()) 
    except: 
        st.write('An Error Has Occured please try again with another file.')           
    st.success("Saved File")
    if st.button('Predict'):
        # global  COUNT
        img = Image.open('tempDir/{}'.format(COUNT))

        try:
            # img.save('static/{}.png'.format(COUNT))
            img_arr = cv2.imread('tempDir/{}'.format(COUNT))

            img_arr = cv2.resize(img_arr, (128,128))
            img_arr = img_arr / 255.0
            img_arr = img_arr.reshape(1, 128,128,3)
            prediction = model.predict(img_arr)

            x = round(prediction[0,0], 2)
            y = round(prediction[0,1], 2)
            preds = np.array([x,y])
            COUNT += 1
            if preds[[1]] > 0.50:
                st.write('It is Dog')
                st.write('Accuracy Score: ')
                st.write('CAT: ',preds[0])
                st.write('DOG: ',preds[1]) 
                
            else:
                st.write('It is Cat')
                st.write('Accuracy Score: ')
                st.write('CAT: {} % '.format(preds[0]))
                st.write('DOG: {} % '.format(preds[1])) 
        except:
            st.write('An Error Has Occured please try again with another file.') 
        
        
           
