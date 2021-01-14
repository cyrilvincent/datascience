import pandas as pd
import sklearn.ensemble as rf
import sklearn.model_selection as ms
import matplotlib.pyplot as plt

dataframe = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
print(dataframe.shape)
y = dataframe.num
x = dataframe.drop("num",1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
model = rf.RandomForestClassifier(n_estimators=100, warm_start=True)
model.fit(xtrain,ytrain)
print(model.score(xtest,ytest))
print(list(zip(x.columns, model.feature_importances_)))

plt.bar(x.columns, model.feature_importances_)
plt.show()

x = x.drop("fbs",1).drop("restecg",1)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
model = rf.RandomForestClassifier(n_estimators=100, warm_start=True)
model.fit(xtrain,ytrain)
print(model.score(xtest,ytest))
print(list(zip(x.columns, model.feature_importances_)))

plt.bar(x.columns, model.feature_importances_)
plt.show()

dataframe = pd.read_csv("data/heartdisease/heart-moredata.csv")
ynew = dataframe.target
xnew = dataframe.drop("target",1).drop("fbs",1).drop("restecg",1).drop("slope", 1).drop("ca", 1).drop("thal", 1)

y = y.append(ynew)
x = x.append(xnew)
print(x.shape)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y, train_size=0.8, test_size=0.2)
model.n_estimators *= 2
model.fit(xtrain,ytrain)
print(model.score(xtest,ytest))