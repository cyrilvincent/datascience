import tensorflow.keras as keras

model = keras.applications.vgg16.VGG16(include_top=False, weights="imagenet", input_shape=(224, 224, 3))

for layer in model.layers[:19]:
    layer.trainable = False

x = model.output
x = keras.layers.Flatten()(x)
x = keras.layers.Dense(256, activation="relu")(x)
x = keras.layers.Dropout(0.2)(x) #0.5, 0.2, 0.1
x = keras.layers.Dense(128, activation="relu")(x)
x = keras.layers.Dropout(0.2)(x)
x =  keras.layers.Dense(30, activation="relu")(x)
x = keras.layers.Dropout(0.2)(x)
#x = keras.layers.Dense(1, activation="sigmoid")(x)
x = keras.layers.Dense(3, activation="softmax")(x)

model = keras.models.Model(inputs=model.input, outputs=x)

model.summary()

model.compile(loss='categorical_crossentropy', #'binary_crossentropy',
              optimizer="rmsprop",
              metrics=['accuracy'])

trainset = keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255, validation_split=0.2,)

batchSize = 16

trainGenerator = trainset.flow_from_directory(
        'data/dogsvscats/train',
        target_size=(224, 224),
        subset = 'training',
        class_mode="categorical",
        batch_size=batchSize)

validationGenerator = trainset.flow_from_directory(
        'data/dogsvscats/train',
        target_size=(224, 224),
        class_mode="categorical",
        subset = 'validation',
        batch_size=batchSize)

model.fit(
        trainGenerator,
        epochs=5,
        validation_data=validationGenerator,
)

model.save('data/dogsvscats/vgg16model-cows.h5')




