import sys
# Include util folder for future use
sys.path.insert(1, '../Util')
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy
import matplotlib.pyplot as plt
from plot_correlation import plot_correlation, plot_densities, plot_hist
from sklearn import preprocessing

import csv
import os


class DataSet():
    data = []
    featureNames = []
    target = []

    def addTrainingData(self, attributes, targetValue):
        self.data.append(attributes)
        self.target.append(targetValue)

    def finalizeDataset(self):
        self.data = numpy.array(self.data, dtype=numpy.float64)
        scaler = preprocessing.QuantileTransformer(output_distribution='normal', random_state=0)
        self.data = scaler.fit_transform(self.data)
        # self.data = preprocessing.Normalizer().fit_transform(self.data)
    
    def setFeatureNames(self, featureNames):
        self.featureNames = featureNames

def doKNN(csvFilePath, featureColumns, targetColumn):
    plot_correlation(csvFilePath, featureColumns + [targetColumn])
    # plot_densities(csvFilePath, featureColumns + [targetColumn], targetColumn)
    dataSet = DataSet()
    with open(os.path.join('.', csvFilePath), 'r') as csvFile:
        dataSet.setFeatureNames(featureColumns)
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            newTrainingDataRow = []
            for feature in featureColumns :
                newTrainingDataRow.append(row[feature])
            dataSet.addTrainingData(newTrainingDataRow, row[targetColumn])
    
    dataSet.finalizeDataset()    
    # plot_hist(dataSet.data)
    X_train,X_test,y_train,y_test = train_test_split(dataSet.data,dataSet.target,test_size=0.2,random_state=4)
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
    

def main(argv):
    csvFilePath = argv[1]
    csvFeatureColumns = argv[2].split(',')
    csvTargetColumn = argv[3]
    doKNN(os.path.join('.', csvFilePath), csvFeatureColumns, csvTargetColumn)

if __name__ == "__main__":
    main(sys.argv)