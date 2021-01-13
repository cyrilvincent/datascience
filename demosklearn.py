import sklearn
import sklearn.linear_model as lm
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn.model_selection as ms
print(sklearn.__version__)

dataset = pd.read_csv("data/house/house.csv")
x = dataset.surface.values.reshape(-1,1)
y = dataset.loyer
np.random.seed(155)
xtrain, xtest, ytrain, ytest = ms.train_test_split(x, y, train_size=0.8, test_size=0.2)

def fit(model, x, y):
    model.fit(x, y)
    return model

def predict(model, x, y):
    print(model.score(x, y))
    plt.scatter(x, y)
    plt.plot(np.arange(400), model.predict(np.arange(400).reshape(-1,1)))
    plt.show()

if __name__ == '__main__':
    #model = lm.LinearRegression()

    model = pipe.make_pipeline(pp.PolynomialFeatures(4), lm.Ridge())
    model = fit(model, xtrain, ytrain)
    predict(model, xtest, ytest)


