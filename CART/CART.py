import sys
sys.path.insert(1, '../PCA')
from doPCA import applyPCA
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

# from '../PCA/doPCA.py' import applyPCA

def applyCart(data, target, report=False):
    model = DecisionTreeClassifier()
    model.fit(data, target)
    if report:
        print('number of classes',model.n_classes_)
        print('number of features',model.n_features_)
        # print(model.tree_)
        expected = dataset.target
        predicted = model.predict(dataset.data)

        print(metrics.classification_report(expected, predicted))
        print(metrics.confusion_matrix(expected, predicted))
    return model

dataset = applyPCA();
applyCart(dataset.data,dataset.target,True);

