
import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn import preprocessing


with open('IST_MIR.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

data1 = pd.read_csv('IST_MIR.csv', delimiter=',')
#data1=(DataFrame)
print(data1)
le = preprocessing.LabelEncoder()


data2=data1.iloc[:,:14]
print(data2)
target = data1['defect_status']
print(target)
data2['org'] = le.fit_transform(data2['org'])
data2['file_'] = le.fit_transform(data2['file_'])



rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
feature_list = list(data2.columns)
#print(data2_list)
features = np.array(data2)
train_features, test_features, train_labels, test_labels = train_test_split(features, target, test_size = 0.25, random_state = 42)


rf.fit(train_features, train_labels);
predictions = rf.predict(test_features)
errors = abs(predictions - test_labels)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
