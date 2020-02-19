import sys
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, KFold
from sklearn import metrics
import numpy
import matplotlib.pyplot as plt
from sklearn import preprocessing

def doLR(X_train, X_test, y_train, y_test, report=False):
    scores_list = []
    precision_score = []
    auc_score = []
    recall_score = []
    f1_score = []
    logisticRegr = LogisticRegression(solver='lbfgs', max_iter=200)
    logisticRegr.fit(X_train, y_train)
    y_pred = logisticRegr.predict(X_test)

    scores_list.append(metrics.accuracy_score(y_test, y_pred))
    precision_score.append(metrics.precision_score(y_test, y_pred))
    try:
        auc_score.append(metrics.roc_auc_score(y_test, y_pred))
    except:
        auc_score.append(0)

    recall_score.append(metrics.recall_score(y_test, y_pred))
    f1_score.append(metrics.f1_score(y_test, y_pred))

    return {'precision': precision_score, 'accuracy': scores_list, 'auc': auc_score, 'recall': recall_score, 'f1_measure': f1_score, 'algorithm' : logisticRegr}
