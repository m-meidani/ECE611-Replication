from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn import preprocessing
import sys
import numpy as np

sys.path.insert(1, '../PCA')


def doCART(dataset, report=False):
    cartData = preprocessing.PowerTransformer(
        standardize=False).fit_transform(dataset.data)
    cv = KFold(n_splits=10)
    k_range = range(1, 26)
    scores_list = []
    precision_score = []
    auc_score = []
    recall_score = []
    f1_score = []
    KthNo = 0
    for train_index, test_index in cv.split(cartData):
        X_train, X_test, y_train, y_test = cartData[train_index], cartData[
            test_index], dataset.target[train_index], dataset.target[test_index]
        model = DecisionTreeClassifier().fit(X_train, y_train)
        y_pred = model.predict(X_test)
        if report:
            KthNo = KthNo+1
            print("--------CART KFOLD #", KthNo)
            print('number of classes', model.n_classes_)
            print('number of features', model.n_features_)
            print('* metrics:')
            print(metrics.classification_report(y_test, y_pred))
            print(metrics.confusion_matrix(y_test, y_pred))

        precision_score.append(metrics.precision_score(y_test, y_pred))
        scores_list.append(metrics.accuracy_score(y_test, y_pred))
        try:
            auc_score.append(metrics.roc_auc_score(y_test, y_pred))
        except:
            auc_score.append(0)
        recall_score.append(metrics.recall_score(y_test, y_pred))
        f1_score.append(metrics.f1_score(y_test, y_pred))
    if report:
        print("precision:", precision_score)
        print("accuracy:", scores_list)
        print("auc_score:", auc_score)
        print("recall_score:", recall_score)
        print("f1_score:", f1_score)
    # now we get the medians
    return {'precision:': np.median(precision_score), 'accuracy:': np.median(scores_list), 'auc:': np.median(auc_score), 'recall:': np.median(recall_score), 'f1_measure:': np.median(f1_score)}
