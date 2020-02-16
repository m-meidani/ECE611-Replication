import pandas as pd
import numpy
from sklearn.cluster import KMeans
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn import metrics
from matplotlib import pyplot as plt


def doKmeans(X_train, X_test, y_train, y_test, report=False):
    scores_list = []
    precision_score = []
    auc_score = []
    recall_score = []
    f1_score = []
    kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_pred = kmeans.fit_predict(X_test)
    precision_score.append(metrics.precision_score(y_test, y_pred))
    try:
        auc_score.append(metrics.roc_auc_score(y_test, y_pred))
    except:
        auc_score.append(0)

    recall_score.append(metrics.recall_score(y_test, y_pred))
    f1_score.append(metrics.f1_score(y_test, y_pred))
    scores_list.append(metrics.accuracy_score(y_test, y_pred))

    return {'precision': precision_score, 'accuracy': scores_list, 'auc': auc_score, 'recall': recall_score,
            'f1_measure': f1_score}

