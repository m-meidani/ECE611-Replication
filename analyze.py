import warnings
warnings.filterwarnings('ignore')
import numpy as np
from sklearn.model_selection import RepeatedKFold

from RandomForests.RF import doRF
from NaiveBayes.NB import doNB
from CART.docart import doCART
from LR.dolr import doLR
from KNN.doknn import doKNN
from PCA.doPCA import applyPCA

PROJECTS = ['Mirantis', 'Mozilla', 'Openstack', 'Wikimedia']
ALGORITHMS = [doCART, doKNN, doLR, doNB, doRF]

algorithm_results = {}

for project in PROJECTS:
    dataSet = applyPCA(project, '.')
    # Log transform data, note that +1 is to avoid zero values
    dataSet.data = np.log(dataSet.data + 1).to_numpy()

    for algorithm in ALGORITHMS:
        precision_score = []
        scores_list = []
        auc_score = []
        recall_score = []
        f1_score = []
        
        rkf = RepeatedKFold(n_splits=10, n_repeats=10, random_state=2652124)
        for train_index, test_index in rkf.split(dataSet.data):
            X_train, X_test, y_train, y_test = dataSet.data[train_index], dataSet.data[test_index], dataSet.target[train_index], dataSet.target[test_index]
            result = algorithm(X_train, X_test, y_train, y_test)
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
        print("[{}] for {} is {}".format(algorithm.__name__, project, algorithm_final_result))