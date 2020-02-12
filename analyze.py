from PCA.doPCA import applyPCA
from KNN.doknn import doKNN

dataSet = applyPCA('Wikimedia', '.')
doKNN(dataSet)