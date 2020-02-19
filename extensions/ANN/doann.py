import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn import metrics

# wine = pd.read_csv('wine_data.csv', names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])


# X = wine.drop('Cultivator',axis=1)
# y = wine['Cultivator']
#train-test  split
def doANN(X_train, X_test, y_train, y_test, externalTest=False ,report=False):
    #preprocess
    scaler=StandardScaler()
    scaler.fit(X_train)
    StandardScaler(copy=True, with_mean=True, with_std=True)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    #training
    mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
    mlp.fit(X_train,y_train)
    
    #prediction
    y_pred = mlp.predict(X_test)
    precision_score = metrics.precision_score(y_test, y_pred)
    scores_list = metrics.accuracy_score(y_test, y_pred)
    try:
        auc_score = metrics.roc_auc_score(y_test, y_pred)
    except:
        auc_score = 0
    recall_score = metrics.recall_score(y_test, y_pred)
    f1_score = metrics.f1_score(y_test, y_pred)
    #report
    if report:
        print('* metrics:')
        print(metrics.classification_report(y_test, y_pred))
        print(metrics.confusion_matrix(y_test, y_pred))
        print("precision:", precision_score)
        print("accuracy:", scores_list)
        print("auc_score:", auc_score)
        print("recall_score:", recall_score)
        print("f1_score:", f1_score)
    return {'precision': precision_score, 'accuracy': scores_list, 'auc': auc_score, 'recall': recall_score, 'f1_measure': f1_score, 'algorithm' : mlp}
    



