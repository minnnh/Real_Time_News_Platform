import tensorflow as tf

EMBEDDING_SIZE = 64
N_FILTERS = 32  # Increased the number of filters
WINDOW_SIZE = 5
FILTER_SHAPE1 = [WINDOW_SIZE, EMBEDDING_SIZE]
FILTER_SHAPE2 = [WINDOW_SIZE, N_FILTERS]
POOLING_WINDOW = 2
POOLING_STRIDE = 2

LEARNING_RATE = 0.001
MAX_DOCUMENT_LENGTH = 380

def generate_cnn_model(n_classes, n_words, max_document_length=MAX_DOCUMENT_LENGTH):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Embedding(input_dim=n_words, output_dim=EMBEDDING_SIZE, input_length=max_document_length))
    model.add(tf.keras.layers.Conv1D(filters=N_FILTERS, kernel_size=WINDOW_SIZE, padding='valid', activation='relu'))
    model.add(tf.keras.layers.MaxPooling1D(pool_size=POOLING_WINDOW, strides=POOLING_STRIDE, padding='same'))
    model.add(tf.keras.layers.Conv1D(filters=N_FILTERS, kernel_size=WINDOW_SIZE, padding='valid', activation='relu'))
    model.add(tf.keras.layers.GlobalMaxPooling1D())
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(n_classes, activation='softmax'))

    optimizer = tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE)
    model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    return model

