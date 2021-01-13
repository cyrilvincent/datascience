import sklearn
import sklearn.linear_model as lm
import sklearn.preprocessing as pp
import sklearn.pipeline as pipe
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print(sklearn.__version__)

dataset = pd.read_csv("data/house/house.csv")
x = dataset.surface.values.reshape(-1,1)
y = dataset.loyer
np.random.seed(155)

def predict(model):
    model.fit(x, y)
    print(model.score(x, y))
    plt.scatter(x, y)
    plt.plot(np.arange(400), model.predict(np.arange(400).reshape(-1,1)))
    plt.show()

if __name__ == '__main__':
    #model = lm.LinearRegression()
    model = pipe.make_pipeline(pp.PolynomialFeatures(8), lm.Ridge())
    predict(model)


