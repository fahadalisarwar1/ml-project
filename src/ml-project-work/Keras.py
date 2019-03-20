import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score
from sklearn.model_selection import train_test_split
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.regularizers import l2
import numpy as np


df = pd.read_csv('/home/fahad/DATA/ML-project/ml-project/data/WorkingData/features_DE_full.csv')
X = df.drop(columns=['FaultType'])
y = df['FaultType']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

X_train.shape
model = Sequential()
model.add(Dense(100, activation='relu', input_dim=10, kernel_regularizer=l2(0.01)))
model.add(Dropout(0.3, noise_shape=None, seed=None))

model.add(Dense(100, activation='relu', kernel_regularizer=l2(0.01)))
model.add(Dropout(0.3, noise_shape=None, seed=None))
model.add(Dense(1, activation='sigmoid'))


# compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


model.summary()
model_output = model.fit(X_train, y_train, epochs=500, batch_size=20, verbose=1, validation_data=(X_test, y_test))


print('training accuracy: ', np.mean(model_output.history['acc']))
print('Validation accuracy: ', np.mean(model_output.history['val_acc']))


y_pred = model.predict(X_test)
precision_score(y_test, y_pred)








