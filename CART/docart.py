from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import numpy as np


def doCART(X_train, X_test, y_train, y_test, report=False,params={}):

    model = DecisionTreeClassifier(**params).fit(X_train, y_train)
    y_pred = model.predict(X_test)
    if report:
        print('number of classes', model.n_classes_)
        print('number of features', model.n_features_)
        print('* metrics:')
        print(metrics.classification_report(y_test, y_pred))
        print(metrics.confusion_matrix(y_test, y_pred))

    precision_score = metrics.precision_score(y_test, y_pred)
    scores_list = metrics.accuracy_score(y_test, y_pred)
    try:
        auc_score = metrics.roc_auc_score(y_test, y_pred)
    except:
        auc_score = 0
    recall_score = metrics.recall_score(y_test, y_pred)
    f1_score = metrics.f1_score(y_test, y_pred)
    if report:
        print("precision:", precision_score)
        print("accuracy:", scores_list)
        print("auc_score:", auc_score)
        print("recall_score:", recall_score)
        print("f1_score:", f1_score)
    # now we get the medians
    return {'precision': precision_score, 'accuracy': scores_list, 'auc': auc_score, 'recall': recall_score, 'f1_measure': f1_score, 'algorithm' : model,'balanced_accuracy':metrics.balanced_accuracy_score(y_test,y_pred)}
