
import csv
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
import numpy
from sklearn import metrics
from sklearn import preprocessing


def doRF(dataSet):
    rfData = preprocessing.PowerTransformer(standardize=False).fit_transform(dataSet.data)
    cv = KFold(n_splits=10)

    precision_score = []
    auc_score = []
    recall_score = []
    f1_score = []

    for train_index, test_index in cv.split(rfData):
        X_train, X_test, y_train, y_test = rfData[train_index], rfData[test_index], dataSet.target[train_index], dataSet.target[test_index]
        rf = RandomForestClassifier()
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)
        precision_score.append(metrics.precision_score(y_test,y_pred))
        try:
            auc_score.append(metrics.roc_auc_score(y_test, y_pred))
        except:
            auc_score.append(0)
        
        recall_score.append(metrics.recall_score(y_test, y_pred))
        f1_score.append(metrics.f1_score(y_test, y_pred))
    
    precision_score = numpy.median(precision_score)
    auc_score = numpy.median(auc_score)
    recall_score = numpy.median(recall_score)
    f1_score = numpy.median(f1_score)

    return (auc_score, precision_score, recall_score, f1_score)
