import sys
import numpy
import csv
import os
import pandas as pd
from sklearn.decomposition import KernelPCA
from sklearn.preprocessing import PowerTransformer, StandardScaler
import numpy as np
import pickle
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

def doKPCA(data, featureColumns, targetColumn):
    dataSet = DataSet()
    df = data.iloc[:,:12]
    dataSet.target = data[targetColumn].to_numpy()
    dataSet.data = df
    df = StandardScaler().fit_transform(df)
    pca = KernelPCA(kernel="rbf", n_components=3)
    principalComponents = pca.fit_transform(df)
    dataSet.components = principalComponents

    return dataSet

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

def applyKPCA(projectName, appDirectory):
    return doKPCA(getData(projectName, appDirectory), CSV_FEATURE_COLUMNS, CSV_TARGET_COLUMNS)