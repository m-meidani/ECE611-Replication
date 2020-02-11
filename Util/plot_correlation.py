import pandas as pd
# import seaborn as sns
#from pylab import rcParams
import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np

def plot_correlation(filePath, featureColumns):
    '''
    plot correlation's matrix to explore dependency between features 
    '''
    # init figure size
    data  = pd.read_csv(filePath, usecols=featureColumns)
    fig = plt.figure()
    # sns.heatmap(data.corr(), annot=True, fmt=".2f")
    plt.show()

def plot_hist(data):
    # x = [item[2] for item in data]
    # print(np.log1p(x))
    # plt.hist(np.log1p(x))
    scaler = preprocessing.QuantileTransformer(output_distribution='normal', random_state=0)
    new_data = scaler.fit_transform(data)
    x = [item[2] for item in new_data]
    print(plt.hist(x))

def plot_densities(filePath, featureColumns, targetColumn):
    '''
    Plot features densities depending on the outcome values
    '''

    data  = pd.read_csv(filePath, usecols=featureColumns)
    # change fig size to fit all subplots beautifully 
    # rcParams['figure.figsize'] = 15, 20

    # separate data based on outcome values 
    outcome_0 = data[data[targetColumn] == 0]
    outcome_1 = data[data[targetColumn] == 1]

    # init figure
    fig, axs = plt.subplots(len(featureColumns), 1)
    fig.suptitle('Features densities for different outcomes 0/1')
    plt.subplots_adjust(left = 0.25, right = 0.9, bottom = 0.1, top = 0.95,
                        wspace = 0.2, hspace = 0.9)

    # plot densities for outcomes
    names = featureColumns
    for column_name in names[:-1]: 
        ax = axs[names.index(column_name)]
        #plt.subplot(4, 2, names.index(column_name) + 1)
        outcome_0[column_name].plot(kind='density', ax=ax, subplots=True, 
                                    sharex=False, color="red", legend=True,
                                    label=column_name + ' for Outcome = 0')
        outcome_1[column_name].plot(kind='density', ax=ax, subplots=True, 
                                     sharex=False, color="green", legend=True,
                                     label=column_name + ' for Outcome = 1')
        ax.set_xlabel(column_name + ' values')
        ax.set_title(column_name + ' density')
        ax.grid('on')
    plt.show()