import sys
import numpy
import csv
import os
import pickle
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import PowerTransformer, StandardScaler
import numpy as np
import matplotlib.pyplot as plt

PROJECT_FILE_NAME = {
    'Mirantis' : 'IST_MIR.csv',
    'Mozilla'  : 'IST_MOZ.csv',
    'Openstack': 'IST_OST.csv',
    'Wikimedia': 'IST_WIK.csv',
    'MinedData': ['MinedData.pckl','ValidMinedData.pckl'],
}

CSV_FEATURE_COLUMNS = ['URL', 'File', 'Lines_of_code', 'Require', 'Ensure', 'Include', 'Attribute',
                         'Hard_coded_string', 'Comment', 'Command', 'File_mode', 'SSH_KEY']
CSV_TARGET_COLUMNS = 'defect_status'

class DataSet():
    data = None
    components = None
    target = None

def doPCA(data, featureColumns, targetColumn, applyTransfer= False , outDF = False, analyzePCA=False, standardize=False):
    dataSet = DataSet()
    # Remove target column
    df = data.iloc[:,:12]
    dataSet.target = data[targetColumn].to_numpy()
    dataSet.data = df
    if applyTransfer:
        df = PowerTransformer(standardize=False).fit_transform(df)
    if standardize:
        df = StandardScaler().fit_transform(df)
    
    df = np.log(df + 1)
    pca = PCA(n_components=0.95, svd_solver='full')
    pca.fit(df)
    principalComponents = pca.transform(df)

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

    return dataSet, pca

def getData(projectName, appDirectory):
    if(projectName not in PROJECT_FILE_NAME):
        raise RuntimeError('INVALID FILE NAME')

    if isinstance(PROJECT_FILE_NAME[projectName], str):
        data = pd.read_csv(os.path.join(appDirectory, 'Dataset', PROJECT_FILE_NAME[projectName]),usecols=CSV_FEATURE_COLUMNS + [CSV_TARGET_COLUMNS])
    else:
        frame=[];
        for file in PROJECT_FILE_NAME[projectName]:
            f = open(os.path.join(appDirectory, 'Dataset',file), 'rb')
            frame.append(pd.DataFrame(pickle.load(f)))
            f.close();
        data = pd.concat(frame)
        data = data.drop(['ID'],axis=1);
        # print(data.keys());
    return data

def applyPCA(projectName=False, appDirectory='.',rawData=False):
    if type(rawData) == type(False):
        return doPCA(getData(projectName, appDirectory), CSV_FEATURE_COLUMNS, CSV_TARGET_COLUMNS, False)
    else:
        return doPCA(rawData, CSV_FEATURE_COLUMNS, CSV_TARGET_COLUMNS, False)

def applyPCAWithStandardize(projectName, appDirectory):
    return doPCA(getData(projectName, appDirectory), CSV_FEATURE_COLUMNS, CSV_TARGET_COLUMNS, False, False, False, True)

# if __name__ == "__main__":
#     print(applyPCA(sys.argv[1], '..'))

