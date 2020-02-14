import sys
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, KFold
from sklearn import metrics
import numpy
import matplotlib.pyplot as plt
from sklearn import preprocessing

from pprint import pprint

import csv
import os


def doLR(dataSet):
    LRData = preprocessing.PowerTransformer(
        standardize=False).fit_transform(dataSet.data)
    cv = KFold(n_splits=10)
    scores = []
    scores_list = []
    precision_score = []
    auc_score = []
    recall_score = []
    f1_score = []
    for train_index, test_index in cv.split(LRData):
        X_train, X_test, y_train, y_test = LRData[train_index], LRData[
            test_index], dataSet.target[train_index], dataSet.target[test_index]
        logisticRegr = LogisticRegression(solver='lbfgs', max_iter=200)
        logisticRegr.fit(X_train, y_train)
        y_pred = logisticRegr.predict(X_test)

        scores.append(metrics.accuracy_score(y_test, y_pred))
        scores_list.append(metrics.accuracy_score(y_test, y_pred))

        precision_score.append(metrics.precision_score(y_test, y_pred))
        try:
            auc_score.append(metrics.roc_auc_score(y_test, y_pred))
        except:
            auc_score.append(0)

        recall_score.append(metrics.recall_score(y_test, y_pred))
        f1_score.append(metrics.f1_score(y_test, y_pred))

        # print(metrics.classification_report(y_test, y_pred))

    precision_score = numpy.median(precision_score)
    auc_score = numpy.median(auc_score)
    recall_score = numpy.median(recall_score)
    f1_score = numpy.median(f1_score)

    return {'precision:': precision_score, 'auc:': auc_score, 'recall:': recall_score, 'f1_measure:': f1_score}
