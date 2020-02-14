import pandas as pd
import numpy
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn import metrics


def doNB(dataSet):
    nbData = preprocessing.PowerTransformer(standardize=False).fit_transform(dataSet.data)

    cv = KFold(n_splits=10)
    precision_score = []
    auc_score = []
    recall_score = []
    f1_score = []
    for train_index, test_index in cv.split(nbData):
        X_train, X_test, y_train, y_test = nbData[train_index], nbData[test_index], dataSet.target[train_index], dataSet.target[test_index]
        gnb = GaussianNB()
        y_pred = gnb.fit(X_train, y_train).predict(X_test)
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

