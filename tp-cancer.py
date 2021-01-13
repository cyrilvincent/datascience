import pandas
import numpy as np

data = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")
np.random.seed(0)

y = data.diagnosis
x = data.drop("diagnosis", 1)

# Knn avec k = 3
# fit, score
# Trouver le k optimum k=1..15
# Humain = 95%