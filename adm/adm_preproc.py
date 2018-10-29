# file: adm_preproc.py
# author: Paul Soma
# description: Functions for preprocessing transaction data for training the anomaly detection model

import definitions
import os


import numpy as np
import pandas as pd
import adm_load as load
from sklearn.model_selection import train_test_split
import adm_datagen as dg
from sklearn.preprocessing import StandardScaler

def preproc(df):
    """
    function to preprocess the raw transaction data into the format needed for training the model
    :param df: pd.DataFrame of transactions
    :return: dfp: pd.DataFrame of preprocessed transactions
    """

    sus_idx = load.get_sus(df)
    fraud_idx = load.get_fraud(df)
    normal_idx = load.get_norm(df)

    amts_sus = dg.gen_post_amounts(df, sus_idx)
    df.update(amts_sus)

    n_sus = len(sus_idx.tolist())
    ones_flags = np.ones(n_sus, dtype='int64')
    sus_ff = pd.DataFrame({'FraudFlag': ones_flags}, index=sus_idx)
    df.update(sus_ff)

    sus_postsuccess = pd.DataFrame({'POSTSUCCESS': ones_flags}, index=sus_idx)
    df.update(sus_postsuccess)

    # drop columns
    df = df.drop(['OURACCOUNT',
                   'LOCALTRANTIME',
                   'LOCALTRANDATE',
                   'TRACENUMBER',
                   'REFERENCENUMBER',
                   'OURTRANSMISSIONTIME',
                   'OURTRANSMISSIONDATE',
                   'OURTRANSMISSIONTIME'
                   ], axis=1)

    df = drop_same(df)

    # addresses

    # normalize

    # deal with categorical features

    # hash account numbers
    acc = df.PROCESSORACCOUNT % 493

    acc_df = pd.DataFrame({'PROCESSORACCOUNT': acc})
    df.update(acc_df)

    df['POSTAMOUNT'] = StandardScaler().fit_transform(df['POSTAMOUNT'].values.reshape(-1, 1))

    df = num_only(df)

    return df



def drop_same(df):
    """
    function to find of any columns which contain only one unique value
    :param: df: pd.DataFrame of transactions
    :return: df_: pd.DataFrame of transactions after dropping columns in to_drop
    """

    to_drop = []
    cols = df.columns

    for c in cols:
        # get the column vector
        cur = df.loc[:, [c]].values
        s = pd.Series(cur.flatten())

        # add to list of cols to drop if col contains one unique value
        if s.nunique() == 1:
            to_drop.append(c)

    df_ = df.drop(to_drop, axis=1)

    return df_


def num_only(df):
    """
    load only numerical columns with nulls filled in as 0
    ignores categorcal fields
    :return: df: a pandas.DataFrame of numerical only transactions
    """
    df = df.select_dtypes(['number'])
    df = df.fillna(0)
    return df


def train_valid_test(df,random_seed):
    """
    function to split the data into training, testing, validation sets
    :param dfn: the preprocessed transaction dataframe
    :param random_seed: a seed for randomly splitting the data
    :return:
    """

    normal = df.loc[df.FraudFlag == 0]
    frauds = df.loc[df.FraudFlag == 1]

    X_train, X_test = train_test_split(normal, test_size=0.2, random_state=random_seed)
    X_train, X_valid = train_test_split(X_train, test_size=0.2, random_state=random_seed)

    # add the fraud cases to test set
    X_test = X_test.append(frauds[0:30])
    X_valid = X_valid.append(frauds[30:])

    # drop the class feature on the train and test data
    y_train = X_train['FraudFlag']
    y_test = X_test['FraudFlag']
    y_valid = X_valid['FraudFlag']

    X_train = X_train.drop(['FraudFlag'], axis=1)
    X_test = X_test.drop(['FraudFlag'], axis=1)
    X_valid = X_valid.drop(['FraudFlag'], axis=1)

    return [X_train, y_train, X_valid, y_valid, X_test, y_test]








