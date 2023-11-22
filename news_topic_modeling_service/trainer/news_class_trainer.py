import news_cnn_model
import numpy as np
import os
import pandas as pd
import pickle
import shutil
import sys
import tensorflow as tf
# import tensorflow.compat.v1 as tf

from sklearn import metrics

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers

import string, re, nltk
# from sklearn import metrics

#from nltk.corpus import stopwords
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'config'))

from news_topic_modeling_service_config import *

# MODEL_OUTPUT_DIR = '../model/'
# DATA_SET_FILE = '../data/labeled_news.csv'
# VARS_FILE = '../model/vars'
# TOKENIZER_SAVE_FILE = '../model/tokenizer_save_file'
# MAX_DOCUMENT_LENGTH = 380
# N_CLASSES = 8

# REMOVE_PREVIOUS_MODEL = False

if os.path.exists(MODEL_OUTPUT_DIR):
    REMOVE_PREVIOUS_MODEL = True

# Training parms
STEPS = 210

def clean_text(text):
    stemmer = PorterStemmer()
    # stop_words = set(stopwords.words('english'))
    stop_words = get_stop_words('en')
    stop_words = get_stop_words('english')
    ## turn to lower case
    text = text.lower()

    ## clean short handed notation
    text = re.sub(r"what's", " what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", " can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", " i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    
    ## clean non alphanumeric chars
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)

    # stem
    # stemmed_tokens = [stemmer.stem(t) for t in word_tokenize(text) if not t in stop_words]
    stemmed_tokens = [stemmer.stem(t) for t in text if not t in stop_words]
    text =  ' '.join(stemmed_tokens)

    return text

def main(unused_argv):
    if REMOVE_PREVIOUS_MODEL:
        # Remove old model
        shutil.rmtree(MODEL_OUTPUT_DIR)
        os.mkdir(MODEL_OUTPUT_DIR)

    # Prepare training and testing data
    df = pd.read_csv(DATA_SET_FILE, header=None)

    # Random shuffle
    df.sample(frac=1)
    X = df[1]
    X = X.apply(lambda x: clean_text(x))

    train_df = df[0:400]
    test_df = df.drop(train_df.index)

    # x - news title, y - class
    x_train = train_df[1]
    y_train = train_df[0]
    x_test = test_df[1]
    y_test = test_df[0]

    # Tokenize and pad the sequences
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(x_train)
    x_train = pad_sequences(tokenizer.texts_to_sequences(x_train), maxlen=MAX_DOCUMENT_LENGTH)
    x_test = pad_sequences(tokenizer.texts_to_sequences(x_test), maxlen=MAX_DOCUMENT_LENGTH)

    # n_words = len(vocab_processor.vocabulary_)
    n_words = len(tokenizer.word_index) + 1
    print('Total words: %d' % n_words)

    # Saving n_words and vocab_processor:
    with open(VARS_FILE, 'wb') as f:
        pickle.dump(n_words, f)

    with open(TOKENIZER_SAVE_FILE, 'wb') as f:
        pickle.dump(tokenizer, f)

    model = news_cnn_model.generate_cnn_model(N_CLASSES, n_words, MAX_DOCUMENT_LENGTH)

    classifier = tf.keras.estimator.model_to_estimator(
        keras_model=model, 
        model_dir=MODEL_OUTPUT_DIR)

    classifier.train(
        input_fn=lambda: tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(1000).batch(32),
        steps=STEPS
    )

    eval_result = classifier.evaluate(
        input_fn=lambda: tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)
    )

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

if __name__ == '__main__':
    tf.compat.v1.app.run(main=main)
    # tf.app.run(main=main)
