import sys
# Include util folder for future use
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, KFold
from sklearn import metrics
import numpy
import matplotlib.pyplot as plt
from sklearn import preprocessing

from pprint import pprint

import csv
import os

def doKNN(dataSet):
    # plot_correlation(csvFilePath, featureColumns + [targetColumn])
    # plot_densities(csvFilePath, featureColumns + [targetColumn], targetColumn)
    # plot_hist(dataSet.data)
    knnData = preprocessing.PowerTransformer(standardize=False).fit_transform(dataSet.data)
    # X_train,X_test,y_train,y_test = train_test_split(knnData,dataSet.target,test_size=0.2,random_state=4)
    cv = KFold(n_splits=10)
    k_range = range(1,26)
    scores = {}
    scores_list = []
    precision_score = []
    auc_score = []
    recall_score = []
    f1_score = []
    for train_index, test_index in cv.split(knnData):
        X_train, X_test, y_train, y_test = knnData[train_index], knnData[test_index], dataSet.target[train_index], dataSet.target[test_index]
        for k in k_range:
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(X_train,y_train)
            y_pred=knn.predict(X_test)
            scores[k] = metrics.accuracy_score(y_test,y_pred)
            scores_list.append(metrics.accuracy_score(y_test,y_pred))
        
            precision_score.append([])
            auc_score.append([])
            recall_score.append([])
            f1_score.append([])
            
            precision_score[k-1].append(metrics.precision_score(y_test,y_pred))
            try:
                auc_score[k-1].append(metrics.roc_auc_score(y_test, y_pred))
            except:
                auc_score[k-1].append(0)
            
            recall_score[k-1].append(metrics.recall_score(y_test, y_pred))
            f1_score[k-1].append(metrics.f1_score(y_test, y_pred))

            # print(metrics.classification_report(y_test, y_pred))
    maxPrecision = 0
    maxAUC = 0
    maxRecall = 0
    maxF1 = 0

    for k in range(0,25):
        precision_score[k] = numpy.median(precision_score[k])
        auc_score[k] = numpy.median(auc_score[k])
        recall_score[k] = numpy.median(recall_score[k])
        f1_score[k] = numpy.median(f1_score[k])

        maxPrecision = max(maxPrecision, precision_score[k])
        maxRecall = max(maxRecall, recall_score[k])
        maxAUC = max(maxAUC, auc_score[k])
        maxF1 = max(maxF1, f1_score[k])

    return (maxAUC, maxPrecision, maxRecall, maxF1)
    

def main(argv):
    csvFilePath = argv[1]
    csvFeatureColumns = argv[2].split(',')
    csvTargetColumn = argv[3]
    doKNN(os.path.join('.', csvFilePath), csvFeatureColumns, csvTargetColumn)

if __name__ == "__main__":
    main(sys.argv)