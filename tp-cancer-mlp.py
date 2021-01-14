import pandas
import numpy as np
import sklearn.tree as tree
import sklearn.neural_network as nn
import sklearn.model_selection as ms
import matplotlib.pyplot as plt
import pickle

data = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")
np.random.seed(0)

y = data.diagnosis
x = data.drop("diagnosis", 1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
model = nn.MLPClassifier(hidden_layer_sizes=(30,10)) # 30 30 10 1
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(model.score(xtest, ytest))

