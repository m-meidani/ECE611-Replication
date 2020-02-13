import warnings
warnings.filterwarnings('ignore')

from PCA.doPCA import applyPCA
from KNN.doknn import doKNN
from LR.dolr import doLR
from NaiveBayes.NB import doNB
from RandomForests.RF import doRF


dataSetMIR = applyPCA('Mirantis', '.')
dataSetMOZ = applyPCA('Mozilla', '.')
dataSetOST = applyPCA('Openstack', '.')
dataSetWIK = applyPCA('Wikimedia', '.')

# print("Mirantis:", doKNN(dataSetMIR))
# print("Mozilla:", doKNN(dataSetMOZ))
# print("Openstack:", doKNN(dataSetOST))
# print("Wikimedia:", doKNN(dataSetWIK))

print("LR Result:")
print("Mirantis:", doLR(dataSetMIR))
print("Mozilla:", doLR(dataSetMOZ))
print("Openstack:", doLR(dataSetOST))
print("Wikimedia:", doLR(dataSetWIK))

print("NB Result:")
print("Mirantis:", doNB(dataSetMIR))
print("Mozilla:", doNB(dataSetMOZ))
print("Openstack:", doNB(dataSetOST))
print("Wikimedia:", doNB(dataSetWIK))

print("RF Result:")
print("Mirantis:", doRF(dataSetMIR))
print("Mozilla:", doRF(dataSetMOZ))
print("Openstack:", doRF(dataSetOST))
print("Wikimedia:", doRF(dataSetWIK))