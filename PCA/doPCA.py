import sys
import numpy
import csv
import os
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import PowerTransformer
import numpy as np
import matplotlib.pyplot as plt

PROJECT_FILE_NAME = {
    'Mirantis' : 'IST_MIR.csv',
    'Mozilla'  : 'IST_MOZ.csv',
    'Openstack': 'IST_OST.csv',
    'Wikimedia': 'IST_WIK.csv'
}

class DataSet():
    data = None
    components = None
    target = None

def doPCA(data, featureColumns, targetColumn, applyTransfer= True , outDF = False, analyzePCA=False):
    dataSet = DataSet()
    # Remove target column
    df = data.iloc[:,:12]
    dataSet.target = data[targetColumn].to_numpy()
    dataSet.data = df
    if applyTransfer:
        df = PowerTransformer(standardize=False).fit_transform(df)
    pca = PCA(n_components=0.95, svd_solver='full')
    principalComponents = pca.fit_transform(df)

    if analyzePCA:
        pca = PCA().fit(dataSet.data)
        print(np.cumsum(pca.explained_variance_ratio_))
        plt.plot(np.cumsum(pca.explained_variance_ratio_))
        plt.xlabel('number of components')
        plt.ylabel('cumulative explained variance')
        plt.show()

    if outDF:
        principalDf = pd.DataFrame(data=principalComponents)
        dataSet.components =  principalDf
    else:
        dataSet.components = principalComponents
    
    # print(dataSet.data.shape)
    # print(len(dataSet.target)

    return dataSet

def applyPCA(projectName, appDirectory):
    if(projectName not in PROJECT_FILE_NAME):
        raise RuntimeError('INVALID FILE NAME')

    csvFeatureColumns = ['URL', 'File', 'Lines_of_code', 'Require', 'Ensure', 'Include', 'Attribute',
                         'Hard_coded_string', 'Comment', 'Command', 'File_mode', 'SSH_KEY']
    csvTargetColumn = 'defect_status'

    data  = pd.read_csv(os.path.join(appDirectory, 'Dataset', PROJECT_FILE_NAME[projectName]),
     usecols=csvFeatureColumns + [csvTargetColumn])

    return doPCA(data, csvFeatureColumns, csvTargetColumn, False)


if __name__ == "__main__":
    print(applyPCA(sys.argv[1], '..'))

