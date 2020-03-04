from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')
from sklearn.exceptions import FitFailedWarning
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
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
from PCA.doPCA import applyPCA, getData, CSV_TARGET_COLUMNS
from PCA.doKPCA import applyKPCA

import pickle
import os

PRINCIPLE_COMPONENT_FINDER = applyPCA
PROJECTS = [ 'Mozilla','Openstack','Mirantis', 'Wikimedia']
# score = 'roc_auc'
score = 'balanced_accuracy'
ALGORITHMS_NAME=[doCART,doKNN,doNB,doRF,doLR]
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
        for boostrap_index in range(0,100):
            # bootstraping
            startTime=time.time()
            print('bootstrap round:',boostrap_index)
            raw_data = getData(project,appDirectory);
            # print(type(raw_data))
            train_data_indexes = np.random.choice(raw_data.shape[0],raw_data.shape[0])
            # print(train_data_indexes)
            train_data = raw_data.loc[train_data_indexes]
            train_data.reset_index(inplace=True)
            test_data = raw_data.drop(np.unique(train_data_indexes))
            test_data.reset_index(inplace=True)
            if test_data.shape[0]==0:
                continue
            #finish bootstraping
            print("# Tuning hyper-parameters->goal {} for {} and {} project".format(score,algo.__name__,project))
            print()
            best_params=[];
            algorithm = ALGORITHMS[algo.__name__]
            dataSet,DimensionReductionModel = PRINCIPLE_COMPONENT_FINDER(rawData=train_data,appDirectory= appDirectory)
            test_data_pc = DimensionReductionModel.transform(test_data.iloc[:,:12])
            test_data_target = test_data[CSV_TARGET_COLUMNS].to_numpy()

            print(np.sum(dataSet.target)/dataSet.target.shape[0])
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
                    'tol':[1e-5,1e-4,1e-3,1e-2,1e-1], #
                    'C': [0.001, 0.1, 1, 10, 100], #
                    'fit_intercept':[True,False], 
                    'solver':[ 'liblinear', 'saga'], 
                    ## 'penalty':[ 'l2' ],
                    ## 'solver':[ 'lbfgs','sag','newton-cg'], 
                    'max_iter':[50,100,150,200],
                    # 'l1_ratio':[1e-5,1e-3,1e-1,0.5],
                    # 'penalty':['elasticnet'],
                    'penalty':['l1', 'l2' ],
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
            # rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=2652124)
            # i=0
            # X_train, X_test, y_train, y_test = train_test_split( dataSet.components, dataSet.target, test_size=0.2, random_state=1)
            X_train = dataSet.components
            y_train = dataSet.target
            X_test = test_data_pc
            y_test = test_data_target

            clf = GridSearchCV(algorithm(), param_grid = GRID_VALUES[algo.__name__],scoring = score,n_jobs=-1,verbose=1,cv=10)
            clf.fit(X_train, y_train)
            print(clf.best_params_)
            # for train_index, test_index in rkf.split(dataSet.components):     
                            # i+=1
                # print('round:',i)
                # X_train, X_test, y_train, y_test = dataSet.components[train_index], dataSet.components[test_index], dataSet.target[train_index], dataSet.target[test_index]    
                # with warnings.catch_warnings():
                #     warnings.simplefilter("ignore",category=FitFailedWarning)
                #     try:
                #         clf.fit(X_train, y_train)
                #     except:
                #         continue
                
                #testing with optimized params
            y_pred = clf.predict(X_test)#, y_train, y_test,params = clf.best_params_)
            try:
                auc_score_op = metrics.roc_auc_score(y_test, y_pred)
            except:
                auc_score_op = 0
            # print("optimized:",metrics.balanced_accuracy_score(y_test,y_pred))
            print("optimized:",auc_score_op)
            precision_score.append(metrics.precision_score(y_test, y_pred))
            scores_list.append(metrics.accuracy_score(y_test, y_pred))
            auc_score.append(auc_score_op)
            recall_score.append(metrics.recall_score(y_test, y_pred))
            f1_score.append(metrics.f1_score(y_test, y_pred))

    #         #testing with default params
            result_no_optim = algo(X_train, X_test, y_train, y_test)
            # print("not optimized:",result_no_optim.get('balanced_accuracy'))
            print('not optimized:',result_no_optim.get('auc'))
            precision_score_no_optim.append(result_no_optim.get('precision'))
            scores_list_no_optim.append(result_no_optim.get('accuracy'))
            auc_score_no_optim.append(result_no_optim.get('auc'))
            recall_score_no_optim.append(result_no_optim.get('recall'))
            f1_score_no_optim.append(result_no_optim.get('f1_measure'))
        best_params.append({'params':clf.best_params_,
            'elapsed_time': time.time() - startTime ,
            'optim_res':{'precision':result_no_optim.get('precision'),'accuracy':result_no_optim.get('accuracy'),'auc':result_no_optim.get('auc'),'recall':result_no_optim.get('recall'),'f1_measure':result_no_optim.get('f1_measure')},
            'defaul_res':{'precision':metrics.precision_score(y_test, y_pred),'accuracy':metrics.accuracy_score(y_test, y_pred),'auc':auc_score_op,'recall':metrics.recall_score(y_test, y_pred),'f1_measure':metrics.f1_score(y_test, y_pred)},
        })

        algorithm_final_result = {'precision:': np.median(precision_score), 
                                    'accuracy:': np.median(scores_list), 
                                    'auc:': np.median(auc_score), 
                                    'recall:': np.median(recall_score), 
                                    'f1_measure:': np.median(f1_score),
                                    'auc_sd':np.std(auc_score),
                                    'auc_avg':np.average(auc_score)
                                    }
        algorithm_final_result_no_optim = {'precision:': np.median(precision_score_no_optim), 
                                    'accuracy:': np.median(scores_list_no_optim), 
                                    'auc:': np.median(auc_score_no_optim), 
                                    'recall:': np.median(recall_score_no_optim), 
                                    'f1_measure:': np.median(f1_score_no_optim),
                                    'auc_sd':np.std(auc_score),
                                    'auc_avg':np.average(auc_score)
                                    }                                            
        #saaving data
        print("[{}] for {} is {}".format(algo.__name__, project, algorithm_final_result))
        f = open('./Optimization_results_bln/'+algo.__name__+'__'+project+'_params.pckl', 'wb')
        print(len(best_params))
        pickle.dump(best_params, f)
        f.close();
        f = open('./Optimization_results_bln/'+algo.__name__+'__'+project+'.pckl', 'wb')
        pickle.dump(algorithm_final_result, f)
        f.close();
        print("[{}] no-optim for {} is {}".format(algo.__name__, project, algorithm_final_result_no_optim))
        f = open('./Optimization_results_bln/'+algo.__name__+'_no_optim__'+project+'.pckl', 'wb')
        pickle.dump(algorithm_final_result_no_optim, f)
        f.close();

f = open('./Optimization_results_bln/finished.pckl', 'wb')
pickle.dump("enjoy the results!", f)
f.close();