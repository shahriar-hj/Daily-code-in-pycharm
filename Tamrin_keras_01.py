# Tamarin Keras prediction Fashion Items
import numpy as np
import tensorflow as tf

mnist = tf.keras.datasets.mnist

class_names = ['T-Shirt/top', 'Trouser', 'pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build Our Model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # 28 because our picture size is this
    tf.keras.layers.Dense(128, activation='relu'),  # 128 fully connected dense layer and ReLu
    tf.keras.layers.Dropout(0.2),  # Turn of Neurons
    tf.keras.layers.Dense(10, activation='softmax')  # 10 DIFFERErent Class for output in softmax
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)

# Evaluate Model
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Tested ACC:", test_acc)

# Ok lets make Prediction
prediction = model.predict(x_test)
print("Our prediction for ", prediction[3], "is", class_names[np.argmax(prediction[3])])
