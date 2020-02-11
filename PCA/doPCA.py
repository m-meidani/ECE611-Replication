import sys
import numpy
import csv
import os
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import PowerTransformer
import numpy as np
import matplotlib.pyplot as plt

sys.path.insert(1, '../Util')




class DataSet():
    data = []
    featureNames = []
    target = []

    def addTrainingData(self, attributes, targetValue):
        self.data.append(attributes)
        self.target.append(targetValue)

    def finalizeDataset(self):
        self.data = numpy.array(self.data, dtype=numpy.float64)
        # scaler = preprocessing.QuantileTransformer(output_distribution='normal', random_state=0)
        # self.data = scaler.fit_transform(self.data)

    def setFeatureNames(self, featureNames):
        self.featureNames = featureNames

def doPCA(csvFilePath, featureColumns, targetColumn, applyTransfer= True , outDF = False, analyzePCA=False):
    dataSet = DataSet()
    for file in csvFilePath:
        with open(os.path.join('.', file), 'r') as csvFile:
            dataSet.setFeatureNames(featureColumns)
            csvReader = csv.DictReader(csvFile)
            for row in csvReader:
                newTrainingDataRow = []
                for feature in featureColumns:
                    newTrainingDataRow.append(row[feature])
                dataSet.addTrainingData(newTrainingDataRow, row[targetColumn])

    dataSet.finalizeDataset();
    # load dataset into Pandas DataFrame
    df = pd.DataFrame(data=dataSet.data, columns=featureColumns)
    if applyTransfer:
        df = PowerTransformer().fit_transform(df)
    pca = PCA(n_components=0.95, svd_solver='full')
    principalComponents = pca.fit_transform(df)

    if analyzePCA:
        pca = PCA().fit(dataSet.data)
        print(np.cumsum(pca.explained_variance_ratio_));
        plt.plot(np.cumsum(pca.explained_variance_ratio_))
        plt.xlabel('number of components')
        plt.ylabel('cumulative explained variance')
        plt.show()

    if outDF:
        principalDf = pd.DataFrame(data=principalComponents)
        dataSet.data =  principalDf;
    else:
        dataSet.data = principalComponents;
    # print(dataSet.data.shape);
    # print(len(dataSet.target);

    return dataSet;



def applyPCA(argv=[]):
    csvFilePath = [
                   # '../Dataset/IST_MIR.csv',
                   # '../Dataset/IST_MOZ.csv',
                   '../Dataset/IST_OST.csv',
                   # '../Dataset/IST_WIK.csv'
                   ]  # argv[1]

    csvFeatureColumns = ['URL', 'File', 'Lines_of_code', 'Require', 'Ensure', 'Include', 'Attribute',
                         'Hard_coded_string', 'Comment', 'Command', 'File_mode', 'SSH_KEY']  # argv[2].split(',')
    csvTargetColumn = 'defect_status'  # argv[3]
    return doPCA(csvFilePath, csvFeatureColumns, csvTargetColumn, False);


# if __name__ == "__main__":
#     print(applyPCA(sys.argv))

