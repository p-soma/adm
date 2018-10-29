# file: adm_datagen.py
# author: Paul Soma
# description: Data generation tools.
#   Functions to pulls random transactions from data, and generate new transactions based on previous ones.
#

import numpy as np
import pandas as pd
from numpy import random


#TODO
def gen_normal(n):
    """
    generate n simulated normal transactions
    query a random transaction
    slightly alter fields by +- epsilon (amount, date, etc.)
    :param n:
    :return:
    """

    return []

#TODO
# generate n random transactions with p% simulated fraudulent
def gen_random(df, p=0.01):

    return []


#TODO
def gen_fraud(df, n):
    """
    anomalize n simulated fraudulent transactions
       switch to a different account with different spending habits
       slightly alter other fields by +- epsilon (amount, date, etc.)
    :param: data the transaction dataset
    :param: n: int number of anomalous transactions to generate
    :return: df: a pandas.DataFrame of the transactions with n 'anomalized' transactions
    """
    # get random transaction

    # increase amount

    # change account and card number to someone who has only US transactions

    # change card acceptor address

    # change date

    pass


def gen_foreign_card_acceptors(df,n):
    """
    function to generate random foreign card acceptors
    used for generating anomalies
    :param: df: pd.DataFrame the transactions
    :param: n: the number of foreign card acceptors to generate
    :return: samp: pd.DataFrame n foreign card acceptor address and ID fields
    """

    # query for foreign card acceptor info
    acceptors = df.loc[df['CARDACCEPTORCOUNTRY'] != 'US',
                       ['CARDACCEPTORCOUNTRY',
                       'CARDACCEPTORIDCODE',
                       'CARDACCEPTORNAME',
                       'CARDACCEPTORSTATE',
                       'CARDACCEPTORSTREET']]

    samp = acceptors.sample(n)

    return samp

#TODO
def gen_rand_account_cards(df):
    """
    function to generate random account and card numbers
    :param: df: the transactions dataframe
    :return: df: pd.DataFrame the transactions to change
    """

    pass

#TODO
def gen_account_card(df, country = 'US'):
    """
    function to get an account and card that only has shopped in the US in the past
    :param country: the specify country the account
    :param df:
    :return: df:
    """

    # get all foreign transactions

    # get all US transactions

    # set difference

    # select accounts and users from the remaining dataframe


    pass

#TODO
def gen_post_amounts(df,idx,lam=10000):
    """
    function to generate random increased POSTAMOUNT on transactions
    :param df: pd.DataFrame
    :param idx: indices for which to generate amounts
    :param lam: multiplier 'how anomalous' should the transactions be?
    :return: amts: pd.DataFrame of new post amounts to use to update transactions
    """

    # number of amounts to generate
    n = len(idx.tolist())


    # generate the amounts
    amts = random.rand(n) * lam
    amts = amts.round(decimals=2)
    amts = pd.DataFrame({'POSTAMOUNT': amts}, index=idx.values)


    return amts


