from RandomForests.RF import doRF
from sklearn.ensemble import RandomForestClassifier
from CART.docart import doCART
from sklearn.tree import DecisionTreeClassifier
from LR.dolr import doLR
from sklearn.linear_model import LogisticRegression
from KNN.simple_doknn import doKNN
from sklearn.neighbors import KNeighborsClassifier
from PCA.doPCA import applyPCA, applyPCAWithStandardize

import pickle
import os

appDirectory='.'
PROJECTS = ['Mirantis', 'Mozilla', 'Openstack', 'Wikimedia']
scores = ['roc_auc']
ALGORITHMS_NAME=[doRF,doLR,doKNN,doCART]

ALGORITHMS = { 
    doCART.__name__: DecisionTreeClassifier, 
    doKNN.__name__: KNeighborsClassifier,
    doLR.__name__: LogisticRegression,
    doRF.__name__: RandomForestClassifier,
 }

f = open('./doCART__Mozilla.pckl', 'rb')
print(pickle.load(f))
f.close()


f = open('./doCART_no_optim__Mozilla.pckl', 'rb')
print(pickle.load(f))
f.close()