from RandomForests.RF import doRF
from sklearn.ensemble import RandomForestClassifier
from CART.docart import doCART
from sklearn.tree import DecisionTreeClassifier
from LR.dolr import doLR
from sklearn.linear_model import LogisticRegression
from KNN.simple_doknn import doKNN
from sklearn.neighbors import KNeighborsClassifier
from NaiveBayes.NB import doNB
from sklearn.naive_bayes import GaussianNB

from PCA.doPCA import applyPCA, applyPCAWithStandardize

import pickle
import os

appDirectory='.'
PROJECTS = [ 'Mozilla', 'Openstack', 'Wikimedia','Mirantis',]
scores = ['roc_auc']
ALGORITHMS_NAME=[doRF,doKNN,doCART,doNB,doLR]

ALGORITHMS = { 
    doCART.__name__: DecisionTreeClassifier, 
    doKNN.__name__: KNeighborsClassifier,
    doLR.__name__: LogisticRegression,
    doRF.__name__: RandomForestClassifier,
 }
for algorithm in ALGORITHMS_NAME:
    for project in PROJECTS:
        f = open('./run_data/{}__{}.pckl'.format(algorithm.__name__,project), 'rb')
        print('op-',project,'-',algorithm.__name__,'=>',pickle.load(f))
        f.close()

        f = open('./run_data/{}_no_optim__{}.pckl'.format(algorithm.__name__,project), 'rb')
        print('def-',project,'-',algorithm.__name__,'=>',pickle.load(f))
        f.close()