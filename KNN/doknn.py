import sys
# Include util folder for future use
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy
import matplotlib.pyplot as plt
from sklearn import preprocessing

import csv
import os

def doKNN(dataSet):
    # plot_correlation(csvFilePath, featureColumns + [targetColumn])
    # plot_densities(csvFilePath, featureColumns + [targetColumn], targetColumn)
    # plot_hist(dataSet.data)
    knnData = preprocessing.Normalizer().fit_transform(dataSet.data)
    X_train,X_test,y_train,y_test = train_test_split(knnData,dataSet.target,test_size=0.2,random_state=4)
    k_range = range(1,26)
    scores = {}
    scores_list = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train,y_train)
        y_pred=knn.predict(X_test)
        scores[k] = metrics.accuracy_score(y_test,y_pred)
        scores_list.append(metrics.accuracy_score(y_test,y_pred))
        # print(metrics.classification_report(y_test, y_pred))
    
    plt.plot(k_range,scores_list)
    plt.xlabel('Value of K for KNN')
    plt.ylabel('Testing Accuracy')
    plt.show()
    print("kkhar")
    

def main(argv):
    csvFilePath = argv[1]
    csvFeatureColumns = argv[2].split(',')
    csvTargetColumn = argv[3]
    doKNN(os.path.join('.', csvFilePath), csvFeatureColumns, csvTargetColumn)

if __name__ == "__main__":
    main(sys.argv)