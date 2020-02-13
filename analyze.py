import warnings
warnings.filterwarnings('ignore')

from PCA.doPCA import applyPCA
from KNN.doknn import doKNN
from LR.dolr import doLR


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