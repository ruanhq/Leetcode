#Wide&Deep Model Architecture:

#Concatenate the wide & deep together here:
input_ = keras.layers.Input(shape = (784, ))
hidden1 = keras.layers.Dense(200, activation = 'relu')(input_)
hidden2 = keras.layers.Dense(200, activation = 'relu')(hidden1)
concat = keras.layers.Concatenate()([input_, hidden3])
output = keras.layers.Dense(10, activation = 'softmax')(concat)
model = keras.Model(inputs = [input_], output = [output])

model.summary()

model.compile(loss = 'sparse_categorical_crossentropy',
	optimizer = 'sgd', metrics = ['accuracy'])
history = model.fit(X_train_full, y_train_full, epochs = 10,
	validation_split = 0.15)
model.evaluate(X_test, y_test)


input_ = keras.layers.Input(shape = (784, ))
hidden1 = keras.layers.Dense(200, activation = 'relu')(input_)

