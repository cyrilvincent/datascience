import pandas
import numpy as np
import sklearn.tree as tree
import sklearn.ensemble as rf
import sklearn.model_selection as ms
import matplotlib.pyplot as plt
import pickle
import xgboost

data = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")
np.random.seed(0)

y = data.diagnosis
x = data.drop("diagnosis", 1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
#model = rf.RandomForestClassifier(n_estimators=100, warm_start=True)
model = xgboost.XGBClassifier(n_estimators=100)
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(model.score(xtest, ytest))

