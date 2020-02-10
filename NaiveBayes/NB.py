import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import preprocessing


from sklearn.naive_bayes import GaussianNB

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

data_train, data_test, target_train,target_test = train_test_split(data2,target, test_size = 0.30, random_state = 10)

gnb = GaussianNB()
pred = gnb.fit(data_train, target_train).predict(data_test)
print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))

