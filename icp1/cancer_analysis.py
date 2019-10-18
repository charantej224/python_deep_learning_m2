import warnings

import numpy as np
import pandas as pd
from keras import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

warnings.simplefilter("ignore")

# Load the train DataFrames using pandas
dataset = pd.read_csv('BreastCancer.csv')

# Fill missing or null values with mean column values in the train set
# Encoding categorical data
labelEncoder = preprocessing.LabelEncoder()
labelEncoder.fit(dataset['diagnosis'])
dataset['diagnosis'] = labelEncoder.transform(dataset['diagnosis'])
dataset.info()
print(dataset.head())

dataset = dataset.values

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, 2:32], dataset[:, 1],
                                                    test_size=0.25, random_state=87)
np.random.seed(155)
sequential_model = Sequential()  # create model
sequential_model.add(Dense(10, input_dim=30, activation='relu'))  # hidden layer
sequential_model.add(Dense(12, activation='softplus'))
# sequential_model.add(Dense(156, activation='sigmoid')) #added one layer
# sequential_model.add(Dense(7, activation='sigmoid')) #added another layer
sequential_model.add(Dense(1, activation='sigmoid'))  # output layer
sequential_model.compile(loss='binary_crossentropy', optimizer='adam')
sequential_model = sequential_model.fit(X_train, Y_train, epochs=100, verbose=0,
                                        initial_epoch=0)
print(sequential_model.summary())
print(sequential_model.evaluate(X_test, Y_test, verbose=0))
# score = accuracy_score(dataset.target, pr)
