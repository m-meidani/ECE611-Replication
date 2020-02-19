import warnings
warnings.filterwarnings('ignore')
import numpy as np
from sklearn.model_selection import RepeatedKFold
import pickle
import os
import pandas as pd
from sklearn import metrics

from RandomForests.RF import doRF
from NaiveBayes.NB import doNB
from CART.docart import doCART
from LR.dolr import doLR
from KNN.doknn import doKNN
from SVM.SVM import doSVM
from extensions.ANN.doann import doANN
from SVM.SVM import doSVM
from Kmeans.Kmeans import doKmeans
from PCA.doPCA import applyPCA, applyPCAWithStandardize
from PCA.doKPCA import applyKPCA

PRINCIPLE_COMPONENT_FINDER = applyPCA#applyKPCA
PROJECTS = ['Mirantis', 'Mozilla', 'Openstack', 'Wikimedia']
ALGORITHMS = [doANN, doCART, doKNN, doLR, doNB, doRF, doSVM, doKmeans]
checkExternalValidity= True
appDirectory='.'

if checkExternalValidity:
    #load defected files
    f = open(os.path.join(appDirectory, 'Dataset','MinedData.pckl'), 'rb')
    minedData = pd.DataFrame(pickle.load(f))
    f.close();
    #load valid files
    f = open(os.path.join(appDirectory, 'Dataset','ValidMinedData.pckl'), 'rb')
    validMinedData = pd.DataFrame(pickle.load(f))
    f.close();
    
for project in PROJECTS:
    dataSet,DimensionReductionModel = PRINCIPLE_COMPONENT_FINDER(project, appDirectory)
    #project the data to same dimensions as project data, using fitted dimensional reduction model
    if checkExternalValidity:
        minedData = minedData[dataSet.data.keys()]
        minedDataComponents = DimensionReductionModel.transform(minedData);
        validMinedData = validMinedData[dataSet.data.keys()]
        validMinedDataComponents = DimensionReductionModel.transform(validMinedData);
        expectedResult = np.concatenate((np.ones(minedDataComponents.shape[0]),np.zeros(validMinedDataComponents.shape[0])),axis=0);
        totalMinedData = np.concatenate((minedDataComponents,validMinedDataComponents),axis=0);

    # Log transform data, note that +1 is to avoid zero values
    # dataSet.data = np.log(dataSet.data + 1).to_numpy()
    for algorithm in ALGORITHMS:
        precision_score = []
        scores_list = []
        auc_score = []
        recall_score = []
        f1_score = []
        
        ext_precision_score = []
        ext_scores_list = []
        ext_auc_score = []
        ext_recall_score = []
        ext_f1_score = []
        rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=2652124)
        for train_index, test_index in rkf.split(dataSet.components):
            X_train, X_test, y_train, y_test = dataSet.components[train_index], dataSet.components[test_index], dataSet.target[train_index], dataSet.target[test_index]
            result = algorithm(X_train, X_test, y_train, y_test)
            precision_score.append(result.get('precision'))
            scores_list.append(result.get('accuracy'))
            auc_score.append(result.get('auc'))
            recall_score.append(result.get('recall'))
            f1_score.append(result.get('f1_measure'))
            trainedModel = result.get('algorithm')
            
            if checkExternalValidity:
                external_pred = trainedModel.predict(totalMinedData)

                ext_precision_score.append(metrics.precision_score(expectedResult, external_pred))
                try:
                    ext_auc_score.append(metrics.roc_auc_score(expectedResult, external_pred))
                except:
                    ext_auc_score.append(0)

                ext_recall_score.append(metrics.recall_score(expectedResult, external_pred))
                ext_f1_score.append(metrics.f1_score(expectedResult, external_pred))
                ext_scores_list.append(metrics.accuracy_score(expectedResult, external_pred))

        algorithm_final_result = {'precision:': np.median(precision_score), 
                                  'accuracy:': np.median(scores_list), 
                                  'auc:': np.median(auc_score), 
                                  'recall:': np.median(recall_score), 
                                  'f1_measure:': np.median(f1_score)
                                  }
        print("[{}] for {} is {}".format(algorithm.__name__, project, algorithm_final_result))
        if checkExternalValidity:
            ext_algorithm_final_result = {'external test precision:': np.median(ext_precision_score), 
                                    'external test accuracy:': np.median(ext_scores_list), 
                                    'external test auc:': np.median(ext_auc_score), 
                                    'external test recall:': np.median(ext_recall_score), 
                                    'external test f1_measure:': np.median(ext_f1_score)
                                    }
            print("External Validity [{}] for the model trained by {} is {}".format(algorithm.__name__, project, ext_algorithm_final_result))