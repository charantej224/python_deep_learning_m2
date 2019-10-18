import pandas as pd
from keras.layers.core import Dense
from keras.models import Sequential
# load dataset
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("diabetes.csv", header=None).values
# print(dataset)

X_train, X_test, Y_train, Y_test = train_test_split(dataset[:, 0:8], dataset[:, 8],
                                                    test_size=0.25, random_state=87)
my_first_nn = Sequential()  # create model
my_first_nn.add(Dense(20, input_dim=8, activation='relu'))  # hidden layer
#my_first_nn.add(Dense(40, activation='relu'))
#my_first_nn.add(Dense(40, activation='relu'))
# my_first_nn.add(Dense(10, activation='softmax')) #added one layer
# my_first_nn.add(Dense(7, activation='softplus')) #added another layer
# my_first_nn.add(Dense(5, activation='relu'))
my_first_nn.add(Dense(1, activation='sigmoid'))  # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam',metrics=['acc'])
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
y_predict = my_first_nn.predict(X_test)
total = len(y_predict)
match = 0
for i in range(len(y_predict)):
    if y_predict[i] == Y_test[i]:
        match += 1
print("total {} matched {} ".format(total, match))

print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))
