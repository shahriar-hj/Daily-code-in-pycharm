# Text Prediction in tensorflow
import tensorflow as tf
from tensorflow import keras
import numpy as np
import tensorflow_hub as hub

print("Version: ", tf.__version__)
print("Eager mode: ", tf.executing_eagerly())
print("Hub version: ", hub.__version__)
print("GPU is", "available" if tf.config.experimental.list_physical_devices("GPU") else "NOT AVAILABLE")

data = tf.keras.datasets.imdb
train_data, validate_data, test_data = data.load_data()
