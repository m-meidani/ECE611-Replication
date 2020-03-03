import pickle
import sys
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

appDirectory='.'
#load defected files
f = open(os.path.join(appDirectory, 'Dataset','MinedData.pckl'), 'rb')
minedData = pd.DataFrame(pickle.load(f))
f.close();
#load valid files
f = open(os.path.join(appDirectory, 'Dataset','ValidMinedData.pckl'), 'rb')
validMinedData = pd.DataFrame(pickle.load(f))
f.close();

# print(validMinedData.shape)
# print(minedData.shape)
fig, axs = plt.subplots(ncols=4,nrows=3)
sns.set(style="whitegrid")


# sns.boxplot(x=minedData["Attribute"], ax=axs[0])
# tips = sns.load_dataset("tips")
# print(tips)
totalData={};

# totalData=pd.concat(frames);
totalData={}

print(minedData.keys());
index=0;
minedData = minedData.drop(['ID','defect_status'],axis=1)
validMinedData = validMinedData.drop(['ID','defect_status'],axis=1)
for key in minedData.keys(): 
    print(key)
    totalData[key]=[minedData[key],validMinedData[key]]
    sns.boxplot(data=totalData[key], orient="h", palette="Set2",ax=axs[int(index/4)][index%4]).set(xlabel=key, ylabel='defect')
    index+=1
# sns.boxplot(x='value',y='valida scripts', data=validMinedData["Attribute"], ax=axs[0])

plt.show()
