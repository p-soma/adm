# file: adm_load.py
# author: Paul Soma
# description: Functions for loading transaction data in the format needed by the models

import pandas as pd
import os

import definitions

def transactions():
    """
    :return: df pandas DataFrame of all transactions
    """
    path = os.path.join(definitions.ROOT_DIR, 'data', 'transactions.csv')

    df = pd.read_csv(path)

    return df

#TODO
def user(our_account):
    """
    Load all transactions from one account
    :param: our_account: the account to load
    :return: df: a numpy_array of transactions from that user
    """
    df = transactions()

    return df

#TODO
def card(df, processor_account):
    """
    Load all transactions from this card
    :param: processor_account:
    :return:
    """

    #return pd.DataFrame()
    pass


def get_fraud(df):
    """
    load suspicious transactions as defined by being flagged as fraud
     or suspected fraud
    :param df: pandas.DataFrame of transactions
    :return:
    """
    # verified fraud
    fraud = df.index[df['FraudFlag'] == 1]

    return fraud

def get_sus(df):
    """


    :param df:
    :return:
    """
    # suspected fraud
    sus = df.index[df['OURRESPONSECODE'] == 2037]

    return sus

def get_norm(df):
    """
    load non suspicious transactions
    :param df:
    :return:
    """
    # normal transactions
    normal = df.index[df['FraudFlag'] == 0]

    return normal




