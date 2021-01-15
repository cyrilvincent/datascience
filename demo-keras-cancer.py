import tensorflow.keras as keras
import pandas
import numpy as np
import sklearn.model_selection as ms
import sklearn.preprocessing as pp

data = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")
np.random.seed(0)

y = data.diagnosis
x = data.drop("diagnosis", 1)

scaler = pp.RobustScaler()
scaler.fit(x)
x = scaler.transform(x)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)

model = keras.Sequential([
    keras.layers.Dense(30, activation="relu",
                       input_shape=(xtrain.shape[1],)),
    keras.layers.Dense(10, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
  ])

model.compile(loss="binary_crossentropy", optimizer="rmsprop",metrics=['accuracy'])
model.summary()

model.fit(xtrain, ytrain, epochs=200, validation_split=0.2)
print(model.evaluate(xtrain, ytrain))
