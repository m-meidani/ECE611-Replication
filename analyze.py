from PCA.doPCA import applyPCA
from KNN.doknn import doKNN

dataSetMIR = applyPCA('Mirantis', '.')
dataSetMOZ = applyPCA('Mozilla', '.')
dataSetOST = applyPCA('Openstack', '.')
dataSetWIK = applyPCA('Wikimedia', '.')

print("Mirantis:", doKNN(dataSetMIR))
print("Mozilla:", doKNN(dataSetMOZ))
print("Openstack:", doKNN(dataSetOST))
print("Wikimedia:", doKNN(dataSetWIK))