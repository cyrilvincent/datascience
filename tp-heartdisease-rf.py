import pandas as pd
import numpy as np
import sklearn.ensemble as rf
import sklearn.model_selection as ms
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
print(dataframe.shape)
y = dataframe.num
x = dataframe.drop("num",1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
model = rf.RandomForestClassifier(n_estimators=100, warm_start=True)
model.fit(x,y)
print(model.score(x,y))
print(list(zip(x.columns, model.feature_importances_)))

plt.bar(x.columns, model.feature_importances_)
plt.show()

x = x.drop("fbs",1).drop("restecg",1)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
model = rf.RandomForestClassifier(n_estimators=100, warm_start=True)
model.fit(x,y)
print(model.score(x,y))
print(list(zip(x.columns, model.feature_importances_)))

plt.bar(x.columns, model.feature_importances_)
plt.show()


