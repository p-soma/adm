"""
file: adm.py
author: Paul Soma
description: anomaly detection model function to run on a transaction
"""


# import libraries


# request data from database

# preprocess data

# load model

# run model on new data

# update database with newly labeled data (fraud/anomaly)

def detect(s):
    """
    wrapper function to apply the entire adm model to a transaction
    :param s: pd.Series
    :return: flag: integer anomaly flag
    """

    # autoencoder


    # isolation forest


    # time-distance frequency check


    # amount check


    # new location check


    # recurring payment check


    flag = 1 if s.fraud_flag == True else 0


    return flag

if __name__ == '__main__':
    print('ok')