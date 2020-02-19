import sys
# Include util folder for future use
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, KFold
from sklearn import metrics
import numpy
import matplotlib.pyplot as plt
from sklearn import preprocessing

def doKNN(X_train, X_test, y_train, y_test):
    # plot_correlation(csvFilePath, featureColumns + [targetColumn])
    # plot_densities(csvFilePath, featureColumns + [targetColumn], targetColumn)
    # plot_hist(dataSet.data)
    # X_train,X_test,y_train,y_test = train_test_split(knnData,dataSet.target,test_size=0.2,random_state=4)
    cv = KFold(n_splits=10)
    k_range = range(1, 26)
    scores_list = []

    precision_score = []
    auc_score = []
    recall_score = []
    f1_score = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        scores_list.append(metrics.accuracy_score(y_test, y_pred))
        precision_score.append(metrics.precision_score(y_test, y_pred))
        try:
            auc_score.append(metrics.roc_auc_score(y_test, y_pred))
        except:
            auc_score.append(0)

        recall_score.append(metrics.recall_score(y_test, y_pred))
        f1_score.append(metrics.f1_score(y_test, y_pred))

        # print(metrics.classification_report(y_test, y_pred))
    return {'precision': max(precision_score), 'accuracy': max(scores_list), 'auc': max(auc_score), 'recall': max(recall_score), 'f1_measure': max(f1_score), 'algorithm' : knn}