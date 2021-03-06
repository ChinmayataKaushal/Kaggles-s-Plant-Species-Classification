# -*- coding: utf-8 -*-
"""CNN#1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/177vgf7BV2Z5CJ3Z39k7OQ9pvPyONjMiP

**TASK - Image Classification using CNNs in Keras**


---

Loading the dataset

Mount your drive here
"""

from google.colab import drive
drive.mount('/content/drive')

"""Importing all libraries here"""

import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from keras.optimizers import Adam
from sklearn.metrics import confusion_matrix, classification_report
from keras.models import load_model
from sklearn.preprocessing import OneHotEncoder
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

"""Loading Dataset i.e., images.npy"""

data = np.load('/content/drive/My Drive/#1/images.npy')
print(data.shape) ## to know the number,shape and channels of images

plt.imshow(data[5]) ## to display any image from the data

"""Image pre-processing"""

images=[]
for img in range(len(data)):
  image = (data[img]/255.0)             ## normalize in 0 to 1
  image = cv2.GaussianBlur(image,(5,5),cv2.BORDER_DEFAULT) ## gaussian blurring
  images.append(image)

images= np.asarray(images)  ## to correct the size of array for further processing

images.shape  ## checking the shape of image dataset

plt.imshow(images[5]) ## to show/check the pre-processing has been done

"""Loading Names of images from names.csv"""

names = pd.read_csv('/content/drive/My Drive/#1/Labels.csv')
print(names)

names['Label'].value_counts() ## to find number of different classes

"""Converting names of images to one-hot-vector for Data Compatibiliy"""

myencoder = OneHotEncoder()
Name = myencoder.fit_transform(names).toarray()
print(type(Name))

print(Name)

## printing data for Name[0]
print(Name[0])

"""Dividing the dataset into training, testing and validating datasets"""

X_train, Xt, y_train, yt = train_test_split(images, Name, test_size=0.3, random_state=7) ## train-test split
X_test, X_val, y_test, y_val = train_test_split(Xt, yt, test_size=0.5, random_state=7) ## test and validation split

X_train.shape ## there are 3325 images in the training set of 128 X 128 dimension having 3 channels

X_test.shape ## there are 712 images in the testing set of 128 X 128 dimension having 3 channels

X_val.shape ## there are 713 images in the validation set of 128 X 128 dimension having 3 channels

"""Making a CNN Model"""

def model():
    ## Convulation and max pooling
    mod= Sequential()
    # 1st layer
    mod.add(Conv2D(64, (3, 3), input_shape = (128, 128, 3), activation = 'relu'))  ## (128,128,3) is our image input size
    mod.add(Conv2D(64, (3, 3), activation = 'relu'))
    mod.add(MaxPooling2D(pool_size = (2, 2),strides=2))
    mod.add(Dropout(0.1))
    # 2nd layer 
    mod.add(Conv2D(64, (3, 3),  activation = 'relu'))
    mod.add(Conv2D(64, (3, 3), activation = 'relu'))
    mod.add(MaxPooling2D(pool_size = (2, 2),strides=2))
    mod.add(Dropout(0.1))
    # 3rd layer 
    mod.add(Conv2D(64, (3, 3), activation = 'relu'))
    mod.add(Conv2D(64, (3, 3), activation = 'relu'))
    mod.add(MaxPooling2D(pool_size = (2, 2)))
    mod.add(Dropout(0.1))

    ## Flatten 
    mod.add(Flatten())

    ## Full connection
    mod.add(Dense(units = 128, activation = 'relu'))
    #mod.add(Dropout(0.2))
    mod.add(Dense(units = 12, activation = 'softmax'))  ## 12 is the number of classes
    ## Compile the model
    mod.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    return mod

Mymodel= model()
Mymodel.summary() ## architecture of the model

"""Fitting the model on Training data and Validating using validation data"""

Mymodel.fit(X_train, y_train, epochs=15, validation_data=(X_val, y_val))

"""Model predictions on Testing data"""

score = Mymodel.evaluate(X_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

####### Analysing dimensions and prediction for 1st image in the dataset #######

#Mymodel.predict_classes(images[0])
print(images[0].shape)
t1 = np.expand_dims(images[0],axis=0)
print(t1.shape)
#print(index(max(Mymodel.predict_classes(t1))))
t2 = Mymodel.predict(t1)
print(myencoder.inverse_transform(t2))

pred = Mymodel.predict_classes(X_test)   ## predicting for the whole test set

"""Predicted Values"""

print(pred)

"""True Values"""

print(y_test)

"""Changing predicted and actual values to be compatible for the confusion matrix"""

ans1 = np.argmax(y_test,axis=1)
print(ans1)

"""Saving this model"""

Mymodel.save('CNNplantclassification.h5')

"""How to load a model"""

####### Mymodel = load_model('path/CNNplantclassification.h5')##########

"""Confusion matrix & Classification report"""

matrix = confusion_matrix(ans1, pred)
clf_report = classification_report(ans1, pred)
print(clf_report)

"""Visualisation for specific values

1. For x_test[2]
"""

#Mymodel.predict_classes(X_test[2])
plt.imshow(X_test[2])
t1 = np.expand_dims(X_test[2],axis=0)
t2 = Mymodel.predict(t1)
t3 = np.expand_dims(y_test[2],axis=0)
print('Prediction:')
print(myencoder.inverse_transform(t2))
print('Actual Class:')
print(myencoder.inverse_transform(t3))

"""2. For x_test[3]"""

#Mymodel.predict_classes(X_test[3])
plt.imshow(X_test[3])
t1 = np.expand_dims(X_test[3],axis=0)
t2 = Mymodel.predict(t1)
t3 = np.expand_dims(y_test[3],axis=0)
print('Prediction:')
print(myencoder.inverse_transform(t2))
print('Actual Class:')
print(myencoder.inverse_transform(t3))

"""3. For x_test[33]"""

#Mymodel.predict_classes(X_test[33])
plt.imshow(X_test[33])
t1 = np.expand_dims(X_test[33],axis=0)
t2 = Mymodel.predict(t1)
t3 = np.expand_dims(y_test[33],axis=0)
print('Prediction:')
print(myencoder.inverse_transform(t2))
print('Actual Class:')
print(myencoder.inverse_transform(t3))

"""4. For x_test[36]"""

#Mymodel.predict_classes(X_test[36])
plt.imshow(X_test[36])
t1 = np.expand_dims(X_test[36],axis=0)
t2 = Mymodel.predict(t1)
t3 = np.expand_dims(y_test[36],axis=0)
print('Prediction:')
print(myencoder.inverse_transform(t2))
print('Actual Class:')
print(myencoder.inverse_transform(t3))

"""5. For x_test[59]"""

#Mymodel.predict_classes(X_test[59])
plt.imshow(X_test[59])
t1 = np.expand_dims(X_test[59],axis=0)
t2 = Mymodel.predict(t1)
t3 = np.expand_dims(y_test[59],axis=0)
print('Prediction:')
print(myencoder.inverse_transform(t2))
print('Actual Class:')
print(myencoder.inverse_transform(t3))