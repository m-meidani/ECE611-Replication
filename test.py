
#further steps for optimization, 
#will be finished later

import lightgbm as lgb
from hyperopt import STATUS_OK
from sklearn.model_selection import RepeatedKFold


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
PROJECTS = ['MinedData','Mirantis', 'Mozilla', 'Openstack', 'Wikimedia']
appDirectory='.'
ALGORITHMS = [ doCART]


project = PROJECTS[0]
algorithm=ALGORITHMS[0]
dataSet,DimensionReductionModel = PRINCIPLE_COMPONENT_FINDER(project, appDirectory)

N_FOLDS = 10


rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=2652124)
for train_index, test_index in rkf.split(dataSet.components):
    X_train, X_test, y_train, y_test = dataSet.components[train_index], dataSet.components[test_index], dataSet.target[train_index], dataSet.target[test_index]
    # Create the dataset
    train_set = lgb.Dataset(X_train, y_train)

def objective(params, n_folds = N_FOLDS):
    """Objective function for Gradient Boosting Machine Hyperparameter Tuning"""
    
    # Perform n_fold cross validation with hyperparameters
    # Use early stopping and evalute based on ROC AUC
    cv_results = lgb.cv(params, train_set, nfold = n_folds, num_boost_round = 10000, 
                        early_stopping_rounds = 100, metrics = 'auc', seed = 50)
  
    # Extract the best score
    best_score = max(cv_results['auc-mean'])
    
    # Loss must be minimized
    loss = 1 - best_score
    
    # Dictionary with information for evaluation
    return {'loss': loss, 'params': params, 'status': STATUS_OK}



    # Sample from the full space
example = sample(space)

# Dictionary get method with default
subsample = example['boosting_type'].get('subsample', 1.0)

# Assign top-level keys
example['boosting_type'] = example['boosting_type']['boosting_type']
example['subsample'] = subsample

example