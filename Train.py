import numpy as np
import tensorflow as tf
from keras import backend as K
from tensorflow.keras.models import Sequential,load_model
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,LSTM
from tensorflow.keras.optimizers import RMSprop, Adam

import pickle
from sklearn.externals import joblib
name = "KerbalSpaceProgramTop"
pickle_in = open("data/"+name+".pickle", "rb")
data = pickle.load(pickle_in)

#loaded_model = joblib.load("data.pickle3")
#result = loaded_model.score()

model = Sequential()

model.add(LSTM(32, input_shape = (data[0].shape[1], data[0].shape[2]), activation='relu',return_sequences = True))
model.add(Dropout(0.2))
model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(data[0].shape[2], activation='softmax'))
model.summary()
model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics = ['accuracy'])
#print(data[1][2].shape)
#for i,_ in enumerate(data[0]):

model.fit((data[0]), (data[1]), epochs = 3, batch_size = 32)
model.save("models/ksptitletop.model")