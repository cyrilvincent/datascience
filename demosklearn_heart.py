import sklearn
import sklearn.linear_model as lm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print(sklearn.__version__)

dataset = pd.read_csv("data/heartdisease/data_cleaned_up.csv")
y = dataset.num
x = dataset.drop("num",axis=1)

def predict(model, x, y):
    model.fit(x, y)
    print(model.score(x, y))

if __name__ == '__main__':
    model = lm.LinearRegression()
    predict(model, x, y)
    print(model.coef_, model.intercept_)


