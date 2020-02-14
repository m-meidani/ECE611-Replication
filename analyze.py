import warnings
warnings.filterwarnings('ignore')
from RandomForests.RF import doRF
from NaiveBayes.NB import doNB
from CART.docart import doCART
from LR.dolr import doLR
from KNN.doknn import doKNN
from PCA.doPCA import applyPCA



dataSetMIR = applyPCA('Mirantis', '.')
dataSetMOZ = applyPCA('Mozilla', '.')
dataSetOST = applyPCA('Openstack', '.')
dataSetWIK = applyPCA('Wikimedia', '.')
# -------------CART
print("")
print("#------------CART Result:")
print("Mirantis:", doCART(dataSetMIR))
print("Mozilla:", doCART(dataSetMOZ))
print("Openstack:", doCART(dataSetOST))
print("Wikimedia:", doCART(dataSetWIK))

# --------------Logistic Regression
print("")
print("#------------LR Result:")
print("Mirantis:", doLR(dataSetMIR))
print("Mozilla:", doLR(dataSetMOZ))
print("Openstack:", doLR(dataSetOST))
print("Wikimedia:", doLR(dataSetWIK))

print("")
print("#------------KNN Result:")
print("Mirantis:", doKNN(dataSetMIR))
print("Mozilla:", doKNN(dataSetMOZ))
print("Openstack:", doKNN(dataSetOST))
print("Wikimedia:", doKNN(dataSetWIK))

print("")
print("#------------NB Result:")
print("Mirantis:", doNB(dataSetMIR))
print("Mozilla:", doNB(dataSetMOZ))
print("Openstack:", doNB(dataSetOST))
print("Wikimedia:", doNB(dataSetWIK))

print("")
print("#------------RF Result:")
print("Mirantis:", doRF(dataSetMIR))
print("Mozilla:", doRF(dataSetMOZ))
print("Openstack:", doRF(dataSetOST))
print("Wikimedia:", doRF(dataSetWIK))
