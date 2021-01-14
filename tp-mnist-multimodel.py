import numpy as np
import sklearn.ensemble as rf
import sklearn.neighbors as nn
import sklearn.svm as svm
import sklearn.neural_network as nn

with np.load("data/mnist/mnist.npz", allow_pickle=True) as f:
    x_train, y_train = f['x_train'], f['y_train']
    x_test, y_test = f['x_test'], f['y_test']

sample = np.random.randint(60000, size=8000)
x_train = x_train[sample]
y_train = y_train[sample]

x_train = x_train.reshape(-1,784)
x_test = x_test.reshape(-1,784)

ESTIMATORS = {
    "Random Forest": rf.RandomForestClassifier(n_estimators=100),
    #"K-nn": nn.KNeighborsClassifier(n_neighbors=3),
    "SVM-poly": svm.SVC(C=0.2, kernel="poly"),
    #"SVM-rbf": svm.SVC(C=0.1, kernel="rbf"),
    "NN": nn.MLPClassifier(hidden_layer_sizes=(500,20)),
}

for key, value in ESTIMATORS.items():
    print(f"Fit model {key}")
    model = value
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    print(f"Model {key}: {score}")

