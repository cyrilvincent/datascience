import tensorflow.keras as keras
import tensorflow as tf

import numpy as np

with np.load("data/mnist/mnist.npz", allow_pickle=True) as f:
    x_train, y_train = f['x_train'], f['y_train']
    x_test, y_test = f['x_test'], f['y_test']

x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
y_train = y_train.astype("float32")
y_test = y_test.astype("float32")

x_train = (x_train - 127.5) / 127.5
x_test /= 255

x_train = x_train.reshape(-1,28*28)
x_test = x_test.reshape(-1,28*28)

sample = np.random.randint(60000, size=60000)
x_train = x_train[sample]
y_train = y_train[sample]

y_cat_train = keras.utils.to_categorical(y_train)
y_cat_test = keras.utils.to_categorical(y_test)

model = keras.Sequential([
    keras.layers.Dense(600, input_shape=(x_train.shape[1],)),
    keras.layers.Dense(400, activation="relu"),
    keras.layers.Dense(200, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(10, activation="softmax"),
  ])

model.compile(loss="categorical_crossentropy", metrics=['accuracy'])
print(model.summary())
trained = model.fit(x_train, y_cat_train, epochs=100, batch_size=1, validation_split=0.2)
predicted = model.predict(x_test)
print(predicted)

import matplotlib.pyplot as plt
# Gestion des erreurs
# on récupère les données mal prédites
predicted[predicted.argmax(axis=1)]
predicted = predicted.argmax(axis=1)
misclass = (y_test != predicted)
images = x_test.reshape((-1, 28, 28))
misclass_images = images[misclass,:,:]
misclass_predicted = predicted[misclass]

# on sélectionne un échantillon de ces images
select = np.random.randint(misclass_images.shape[0], size=12)

# on affiche les images et les prédictions (erronées) associées à ces images
for index, value in enumerate(select):
    plt.subplot(3,4,index+1)
    plt.axis('off')
    plt.imshow(misclass_images[value],cmap=plt.cm.gray_r,interpolation="nearest")
    plt.title('Predicted: %i' % misclass_predicted[value])

plt.show()

# ytrain = [1,8,5] shape(3) = shape(3,1)
# predict = 1 = [0,1.0,0,0,0,0,0,0,0,0]
#           8 = [0,0,0,0,0,0,0,0,0,1,0]
#           5 = [0,0,0,0,0,1,0,0,0,0,0]
#[[0,1.0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,0]] shape(3,10)
#to_categorical transforme le shape(3,1) et (3,10)