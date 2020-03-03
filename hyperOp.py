
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import numpy as np
from sklearn.model_selection import RepeatedKFold, train_test_split
import pickle
import os
import pandas as pd
from sklearn import metrics
import time
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
from PCA.doPCA import applyPCA, getData
from PCA.doKPCA import applyKPCA

import pickle
import os

PRINCIPLE_COMPONENT_FINDER = applyPCA
PROJECTS = ['Mirantis', 'Mozilla', 'Openstack', 'Wikimedia']
score = 'roc_auc'
ALGORITHMS_NAME=[doLR,doCART,doKNN,doNB,doRF]
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
        print("# Tuning hyper-parameters->goal {} for {} and {} project".format(score,algo.__name__,project))
        print()
        best_params=[];
        algorithm = ALGORITHMS[algo.__name__]
        dataSet,DimensionReductionModel = PRINCIPLE_COMPONENT_FINDER(project, appDirectory)
        # X_train=dataSet.components
        # y_train= dataSet.target
        max_iter = ['log2','sqrt',None]
        GRID_VALUES={
            doCART.__name__:{
                'criterion':['gini','entropy'],
                'splitter':['best', 'random'],
                'min_samples_split':[2,5,8,10,100],
                'min_samples_leaf':[1,3,6,10,100],
                'min_weight_fraction_leaf':[0.0001, 0.001, 0.01, 0.1, 0.49],
                'max_features': ['log2','sqrt',None],
                # 'max_features': ['log2','sqrt',None,*list(range(1,dataSet.components.shape[1],2))],
            },
            doNB.__name__:{
            },
            doKNN.__name__:{
                'n_neighbors':[*list(range(1,max(int(dataSet.components.shape[0]**(0.5)),17),4))], #
                'weights':['uniform','distance'],
                'algorithm':['auto', 'ball_tree', 'kd_tree', 'brute'],
                'leaf_size':[*list(range(10,50,10))],
            },
            doLR.__name__:{
                'penalty':['l1', 'l2', 'elasticnet'],
                'dual':[True,False],
                'tol':[1e-5,1e-4,1e-3,1e-2,1e-1], #
                'C': [0.001, 0.1, 1, 10, 100], #
                'fit_intercept':[True,False], 
                'solver':['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'], 
                'max_iter':[50,100,150,200],
                'l1_ratio':[1e-5,1e-3,1e-1,0.5],
            },
            doRF.__name__:{
                'n_estimators':[*list(range(10,50,10))], ##
                'criterion':['gini','entropy'],
                'min_samples_split':[2,5,8,10,100],
                # 'min_samples_split':[2,4,6,8,10], #
                'min_samples_leaf':[1,3,6,10,100],
                # 'min_samples_leaf':[1,2,3,4,5,6],   #
                'min_weight_fraction_leaf':[0.0001, 0.001, 0.01, 0.1, 0.49], 
                'max_features': ['log2','sqrt',None],
            }
        }
        precision_score = []
        scores_list = []
        auc_score = []
        recall_score = []
        f1_score = []

        precision_score_no_optim = []
        scores_list_no_optim = []
        auc_score_no_optim = []
        recall_score_no_optim = []
        f1_score_no_optim = []

        rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=2652124)
        i=0

        for train_index, test_index in rkf.split(dataSet.components):     
            startTime=time.time()
            i+=1
            print('round:',i)
            X_train, X_test, y_train, y_test = dataSet.components[train_index], dataSet.components[test_index], dataSet.target[train_index], dataSet.target[test_index]    
            clf = GridSearchCV(algorithm(), param_grid = GRID_VALUES[algo.__name__],scoring = score,n_jobs=-1,verbose=1)
            clf.fit(X_train, y_train)
            print(clf.best_params_)
            
            #testing with optimized params
            result = algo(X_train, X_test, y_train, y_test,params = clf.best_params_)
            precision_score.append(result.get('precision'))
            scores_list.append(result.get('accuracy'))
            auc_score.append(result.get('auc'))
            recall_score.append(result.get('recall'))
            f1_score.append(result.get('f1_measure'))

            #testing with default params
            result_no_optim = algo(X_train, X_test, y_train, y_test)
            precision_score_no_optim.append(result_no_optim.get('precision'))
            scores_list_no_optim.append(result_no_optim.get('accuracy'))
            auc_score_no_optim.append(result_no_optim.get('auc'))
            recall_score_no_optim.append(result_no_optim.get('recall'))
            f1_score_no_optim.append(result_no_optim.get('f1_measure'))
            best_params.append({'params':clf.best_params_,
                'elapsed_time': time.time() - startTime ,
                'optim_res':{'precision':result_no_optim.get('precision'),'accuracy':result_no_optim.get('accuracy'),'auc':result_no_optim.get('auc'),'recall':result_no_optim.get('recall'),'f1_measure':result_no_optim.get('f1_measure')},
                'defaul_res':{'precision':result.get('precision'),'accuracy':result.get('accuracy'),'auc':result.get('auc'),'recall':result.get('recall'),'f1_measure':result.get('f1_measure')},
            })

        algorithm_final_result = {'precision:': np.average(precision_score), 
                                    'accuracy:': np.average(scores_list), 
                                    'auc:': np.average(auc_score), 
                                    'recall:': np.average(recall_score), 
                                    'f1_measure:': np.average(f1_score),
                                    'auc_sd':np.std(auc_score)
                                    }
        algorithm_final_result_no_optim = {'precision:': np.average(precision_score_no_optim), 
                                    'accuracy:': np.average(scores_list_no_optim), 
                                    'auc:': np.average(auc_score_no_optim), 
                                    'recall:': np.average(recall_score_no_optim), 
                                    'f1_measure:': np.average(f1_score_no_optim),
                                    'auc_sd':np.std(auc_score_no_optim)
                                    }                                            
        #saaving data
        print("[{}] for {} is {}".format(algo.__name__, project, algorithm_final_result))
        f = open('./Optimization_results/'+algo.__name__+'__'+project+'_params.pckl', 'wb')
        print(len(best_params))
        pickle.dump(best_params, f)
        f.close();
        f = open('./Optimization_results/'+algo.__name__+'__'+project+'.pckl', 'wb')
        pickle.dump(algorithm_final_result, f)
        f.close();
        print("[{}] no-optim for {} is {}".format(algo.__name__, project, algorithm_final_result_no_optim))
        f = open('./Optimization_results/'+algo.__name__+'_no_optim__'+project+'.pckl', 'wb')
        pickle.dump(algorithm_final_result_no_optim, f)
        f.close();

f = open('./Optimization_results/finished.pckl', 'wb')
pickle.dump("enjoy the results!", f)
f.close();