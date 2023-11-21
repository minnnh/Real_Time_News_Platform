import numpy as np
import os
import pandas as pd
import pickle
import sys
import tensorflow as tf
import time
import news_classes

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'trainer'))
from news_cnn_model import generate_cnn_model
from news_class_trainer import clean_text

MODEL_DIR = '../model'
MODEL_UPDATE_LAG_IN_SECONDS = 10

N_CLASSES = 8

VARS_FILE = '../model/vars'
TOKENIZER_SAVE_FILE = '../model/tokenizer_save_file'

n_words = 0

MAX_DOCUMENT_LENGTH = 500

classifier = None
tokenizer = None  # Added

def restore_vars():
    with open(VARS_FILE, 'rb') as f:
        global n_words
        n_words = pickle.load(f)

def load_tokenizer():
    with open(TOKENIZER_SAVE_FILE, 'rb') as f:
        global tokenizer
        tokenizer = pickle.load(f)

def load_model():
    global classifier
    model = generate_cnn_model(N_CLASSES, n_words, MAX_DOCUMENT_LENGTH)
    classifier = tf.keras.estimator.model_to_estimator(keras_model=model, model_dir=MODEL_DIR)

    # Since the model is not trained further in this file, you can skip the evaluation step.

    print("Model update.")

def input_fn(x):
    dataset = tf.data.Dataset.from_tensor_slices(x)
    dataset = dataset.batch(32)
    return dataset

restore_vars()
load_tokenizer()  # Added
load_model()

print("Model loaded.")

class ReloadModelHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        # Reload model
        print("Model update detected. Loading new model.")
        time.sleep(MODEL_UPDATE_LAG_IN_SECONDS)
        restore_vars()
        load_tokenizer()  # Added
        load_model()

# Setup watchdog
observer = Observer()
observer.schedule(ReloadModelHandler(), path=MODEL_DIR, recursive=False)
observer.start()

def classify(text):
    text = clean_text(text)
    data = np.array([text])
    data = tokenizer.texts_to_sequences(data)
    data = pad_sequences(data, maxlen=MAX_DOCUMENT_LENGTH)

    # Assuming classifier is a tf.keras.Model
    y_predicted = classifier.predict(input_fn=lambda: input_fn(data, np.zeros(len(data))))

    # Assuming news_classes.class_map is defined somewhere in your code
    topic = news_classes.class_map[str(np.argmax(y_predicted) + 1)]
    return topic




# def input_fn(x):
#     dataset = tf.data.Dataset.from_tensor_slices(x)
#     dataset = dataset.batch(32)
#     return dataset


def test_basic():
    newsTitle = "8 reasons Andrew Puzder's nomination is a mess"
    topic = classify(newsTitle)
    print(topic)
    assert topic == "U.S."
    print('test_basic passed!')

if __name__ == "__main__":
    test_basic()


