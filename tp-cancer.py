import pandas
import numpy as np
import sklearn.neighbors as nn
import sklearn.model_selection as ms

data = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")
np.random.seed(0)

y = data.diagnosis
x = data.drop("diagnosis", 1)

# Knn avec k = 3
# fit, score
# Trouver le k optimum k=1..15
# Humain = 95%

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
# for k in range(1,16):
#     model = nn.KNeighborsClassifier(n_neighbors=k)
#     model.fit(xtrain, ytrain)
#     print(k, model.score(xtest, ytest))
model = nn.KNeighborsClassifier(n_neighbors=8)
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))

# Pro : Simple, White box, peu sensible aux données non normalisée
# Cons : Couteux en prédiction et en mémoire, dépendant le la taille du trainingset, categoristation, peu universaliste