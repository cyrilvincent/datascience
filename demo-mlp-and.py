import numpy as np
import sklearn.neural_network

X=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([-1,-1,-1,1]) # 0 center

model = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(4,8)) # 2 4 8 1
model.fit(X, y)
res = model.predict(X)
print(res)
print(res > 0)