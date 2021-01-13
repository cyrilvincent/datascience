import pandas
import numpy as np
import sklearn.neighbors as nn
import sklearn.model_selection as ms

data = pandas.read_csv("data/breast-cancer/data.csv", index_col="id")
np.random.seed(0)

y = data.diagnosis
x = data.drop("diagnosis", 1)

xtrain, xtest, ytrain, ytest = ms.train_test_split(x,y,train_size=0.8, test_size=0.2)
model = nn.KNeighborsClassifier(n_neighbors=8)
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))

# Pro : Simple, White box, peu sensible aux données non normalisée
# Cons : Couteux en prédiction et en mémoire, dépendant le la taille du trainingset, categoristation, peu universaliste