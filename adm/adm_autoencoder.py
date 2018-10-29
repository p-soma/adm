"""
file: adm_autoencoder.py
author: Paul Soma
description: Autoencoder anomaly detection model
"""
import definitions


# package imports
from keras.models import Model
from keras.layers import Input, Dense
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras import regularizers
import pickle
import uuid

# local module imports
import adm_load
import adm_preproc

def train_autoencoder(nb_epoch=10):

    # load all transaction data from csv
    df = adm_load.transactions()

    dfn = adm_preproc.preproc(df)

    # split the data into training, validation and test sets

    splits = adm_preproc.train_valid_test(dfn, definitions.RANDOM_SEED)
    X_train, y_train, X_valid, y_valid, X_test, y_test = splits

    X_train = X_train.values
    X_test = X_test.values
    X_valid = X_valid.values


    input_dim = X_train.shape[1]  # number of features

    # num neurons in first encoding layer
    encoding_dim = 12

    # input layer
    input_layer = Input(shape=(input_dim,))

    # 12 neuron encoding layer
    encoder = Dense(encoding_dim, activation='tanh',
                    activity_regularizer=regularizers.l1(10e-5))(input_layer)
    # 6 neuron encoding layer
    encoder = Dense(int(encoding_dim / 2), activation='relu')(encoder)

    # 6 neuron decoding layer
    decoder = Dense(int(encoding_dim / 2), activation='tanh')(encoder)

    # 26 layer decoding layer (output layer, predicts all features)
    decoder = Dense(input_dim, activation='relu')(decoder)

    # put it all together
    autoencoder = Model(inputs=input_layer, outputs=decoder)


    batch_size = 32  # number of samples per gradient update


    autoencoder.compile(optimizer='adam',
                        loss='mean_squared_error',
                        metrics=['accuracy'])

    model_id = str(uuid.uuid4())
    model_filepath = './model_checkpoints/autoencoder-' + model_id + '.h5'

    checkpointer = ModelCheckpoint(filepath=model_filepath,
                                   verbose=0,
                                   save_best_only=True)

    tensorboard = TensorBoard(log_dir='./logs',
                              histogram_freq=0,
                              write_graph=True,
                              write_images=True)

    # fit the model to itself and save training history
    # we also save a checkpoint of the model after each training step
    history = autoencoder.fit(X_train, X_train,
                              epochs=nb_epoch,
                              batch_size=batch_size,
                              shuffle=True,
                              validation_data=(X_valid, X_valid),
                              verbose=1,
                              callbacks=[checkpointer, tensorboard]).history


    history_filepath = './model_checkpoints/autoencoder-history-' + model_id
    with open(history_filepath, 'wb') as file_pi:
        pickle.dump(history, file_pi)


    print('ok')

