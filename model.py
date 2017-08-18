from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import to_categorical
import get_params
import numpy as np


from keras.layers import Embedding
from keras.layers import LSTM

# For a single-input model with 10 classes (categorical classification):

x_train = get_params.pre_processed_data
y_train = get_params.labels
#x_test = np.random.random((20, 100, 100, 3))
#y_test = keras.utils.to_categorical(np.random.randint(10, size=(20, 1)), num_classes=10)




model = Sequential()
model.add(Embedding(23, output_dim=200))
model.add(LSTM(
        input_dim=200,
        output_dim=100,
        return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(
        input_dim=50,
        output_dim=20,
        return_sequences=True))
model.add(Dropout(0.2))



model.add(Dense(
        output_dim=1))
model.add(Activation("linear"))


model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=32, epochs=100)