
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import numpy as np
from sklearn.model_selection import RepeatedKFold
import pickle
import os
import pandas as pd
from sklearn import metrics

from RandomForests.RF import doRF
from sklearn.ensemble import RandomForestClassifier
from NaiveBayes.NB import doNB
from sklearn.naive_bayes import GaussianNB
from CART.docart import doCART
from sklearn.tree import DecisionTreeClassifier
from LR.dolr import doLR
from sklearn.linear_model import LogisticRegression
from KNN.simple_doknn import doKNN
from sklearn.neighbors import KNeighborsClassifier
# from SVM.SVM import doSVM
# from sklearn import svm
# from extensions.ANN.doann import doANN
# from sklearn.neural_network import MLPClassifier
# from Kmeans.Kmeans import doKmeans
from PCA.doPCA import applyPCA, applyPCAWithStandardize
from PCA.doKPCA import applyKPCA

import pickle
import os

PRINCIPLE_COMPONENT_FINDER = applyPCA
PROJECTS = ['Mirantis', 'Mozilla', 'Openstack', 'Wikimedia']
scores = ['f1']
ALGORITHMS_NAME=[doNB,doLR,doKNN,doCART,doRF]
ALGORITHMS = { 
    doCART.__name__: DecisionTreeClassifier, 
    doNB.__name__: GaussianNB,  
    doKNN.__name__: KNeighborsClassifier,
    doLR.__name__: LogisticRegression,
    doRF.__name__: RandomForestClassifier,
 }
appDirectory='.'
step=20

for algo in ALGORITHMS_NAME:
    for project in PROJECTS:
        algorithm = ALGORITHMS[algo.__name__]
        dataSet,DimensionReductionModel = PRINCIPLE_COMPONENT_FINDER(project, appDirectory)
        X_train=dataSet.components
        y_train= dataSet.target

        max_iter = ['log2','sqrt',None]
        GRID_VALUES={
            doCART.__name__:{
                'criterion':['gini','entropy'],
                'splitter':['best', 'random'],
                'min_samples_split':[2,3,4,5,6,7,8,9,10],
                'min_samples_leaf':[1,2,3,4,5,6],
                'min_weight_fraction_leaf':[0.01,0.1,0.2,0.3,0.4,0.49],
                'max_features': ['log2','sqrt',None,*list(range(1,dataSet.components.shape[1]))],
            },
            doNB.__name__:{
            },
            doKNN.__name__:{
                'n_neighbors':[*list(range(1,int(dataSet.components.shape[0]**(0.5))))],
                'weights':['uniform','distance'],
                'algorithm':['auto', 'ball_tree', 'kd_tree', 'brute'],
                'leaf_size':[*list(range(1,dataSet.components.shape[0],step))],
                'n_jobs':[10]
            },
            doLR.__name__:{
                'penalty':['l1', 'l2', 'elasticnet'],
                'dual':[True,False],
                'tol':[1e-5,1e-4,1e-3,1e-2,1e-1],
                'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
                'fit_intercept':[True,False],
                'solver':['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
                'max_iter':[30,50,80,100,150,200],
                'multi_class':['auto', 'ovr', 'multinomial'],
                'l1_ratio':[1e-5,1e-4,1e-3,1e-2,1e-1],
                'n_jobs':[10],
            },
            doRF:{
                'n_estimators':[*list(range(1,dataSet.components.shape[0],step))],
                'criterion':['gini','entropy'],
                'min_samples_split':[2,3,4,5,6,7,8,9,10],
                'min_samples_leaf':[1,2,3,4,5,6],
                'min_samples_leaf':[1,2,3,4,5,6],
                'min_weight_fraction_leaf':[0.01,0.1,0.2,0.3,0.4,0.49],
                'max_features': ['log2','sqrt',None,*list(range(1,dataSet.components.shape[1]))],
            }
        }

        rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=2652124)
        for score in scores:
            print("# Tuning hyper-parameters->goal {} for {} and {} project".format(score,algo.__name__,project))
            print()
            clf = GridSearchCV(algorithm(), param_grid = GRID_VALUES[algo.__name__],scoring = score,n_jobs=-1,cv=10)
            clf.fit(X_train, y_train)
            print("Best parameters set found on development set:")
            print()
            print(clf.best_params_)
            print()
            # print("Grid scores on development set:")
            # print()
            means = clf.cv_results_['mean_test_score']
            stds = clf.cv_results_['std_test_score']

        
        precision_score = []
        scores_list = []
        auc_score = []
        recall_score = []
        f1_score = []
        rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=2652124)
        for train_index, test_index in rkf.split(dataSet.components):
            X_train, X_test, y_train, y_test = dataSet.components[train_index], dataSet.components[test_index], dataSet.target[train_index], dataSet.target[test_index]    
            result = algo(X_train, X_test, y_train, y_test,params = clf.best_params_)
            precision_score.append(result.get('precision'))
            scores_list.append(result.get('accuracy'))
            auc_score.append(result.get('auc'))
            recall_score.append(result.get('recall'))
            f1_score.append(result.get('f1_measure'))
        algorithm_final_result = {'precision:': np.median(precision_score), 
                                    'accuracy:': np.median(scores_list), 
                                    'auc:': np.median(auc_score), 
                                    'recall:': np.median(recall_score), 
                                    'f1_measure:': np.median(f1_score)
                                    }
        print("[{}] for {} is {}".format(algo.__name__, project, algorithm_final_result))
        f = open('./Optimization_results/'+algo.__name__+'__'+project+'.pckl', 'wb')
        pickle.dump(algorithm_final_result, f)
        f.close();

        precision_score_no_optim = []
        scores_list_no_optim = []
        auc_score_no_optim = []
        recall_score_no_optim = []
        f1_score_no_optim = []
        for train_index, test_index in rkf.split(dataSet.components):
            X_train, X_test, y_train, y_test = dataSet.components[train_index], dataSet.components[test_index], dataSet.target[train_index], dataSet.target[test_index]    
            result = algo(X_train, X_test, y_train, y_test)
            precision_score_no_optim.append(result.get('precision'))
            scores_list_no_optim.append(result.get('accuracy'))
            auc_score_no_optim.append(result.get('auc'))
            recall_score_no_optim.append(result.get('recall'))
            f1_score_no_optim.append(result.get('f1_measure'))
        algorithm_final_result_no_optim = {'precision:': np.median(precision_score_no_optim), 
                                    'accuracy:': np.median(scores_list_no_optim), 
                                    'auc:': np.median(auc_score_no_optim), 
                                    'recall:': np.median(recall_score_no_optim), 
                                    'f1_measure:': np.median(f1_score_no_optim)}
        print("[{}] no-optim for {} is {}".format(algo.__name__, project, algorithm_final_result_no_optim))
        f = open('./Optimization_results/'+algo.__name__+'_no_optim__'+project+'.pckl', 'wb')
        pickle.dump(algorithm_final_result_no_optim, f)
        f.close();

