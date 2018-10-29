"""
file: adm_isolation_forest.py
author: Paul Soma
description: Isolation forest anomaly detection model
"""

from sklearn.ensemble import IsolationForest

import adm_load
import adm_preproc



# Work in progress
def train_isolation_forest():
    """
    function to train an isolation forest
    :return:
    """
    # load all transaction data from csv
    df = adm_load.transactions()

    dfn = adm_preproc.preproc(df)

    splits = adm_preproc.train_valid_test(dfn, RANDOM_SEED)
    X_train, y_train, X_valid, y_valid, X_test, y_test = splits

    model = IsolationForest(random_state=42,
                            n_estimators=100,
                            max_samples=X_train.shape[0],
                            bootstrap=True,)

    model.fit(X_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    score = model.decision_function(X_valid)
    outliers = model.predict(X_valid)


    return score


