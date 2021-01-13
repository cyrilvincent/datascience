import pandas
import numpy as np
import sklearn.tree as tree
import sklearn.ensemble as rf
import sklearn.model_selection as ms
import matplotlib.pyplot as plt
import pickle

data = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")
np.random.seed(0)

y = data.diagnosis
x = data.drop("diagnosis", 1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
model = rf.RandomForestClassifier(n_estimators=100, warm_start=True)
model.fit(xtrain, ytrain)
score = model.score(xtest, ytest)
print(model.score(xtest, ytest))

with open(f"data/cancer-rf-{score:.2f}.pickle","wb") as f:
    pickle.dump(model, f)

model = None

with open("data/cancer-rf.pickle","rb") as f:
    model = pickle.load(f)

predicted = model.predict(xtest)
delta = predicted - ytest
print(delta.values)

print(model.feature_importances_)
print(x.columns)
print(list(zip(x.columns, model.feature_importances_)))

plt.bar(x.columns, model.feature_importances_)
plt.show()

plt.figure()
tree.plot_tree(model.estimators_[0],
                feature_names = x.columns,
                # class_names = cancer.target_names,
                rounded = True, proportion = True,
                precision = 2, filled = True)
plt.show()