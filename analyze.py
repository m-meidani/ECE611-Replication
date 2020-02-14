from CART.docart import doCART
from LR.dolr import doLR
from KNN.doknn import doKNN
from PCA.doPCA import applyPCA
import warnings
warnings.filterwarnings('ignore')


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
# -------------KNN
print("")
print("#------------KNN Result:")
print("Mirantis:", doKNN(dataSetMIR))
print("Mozilla:", doKNN(dataSetMOZ))
print("Openstack:", doKNN(dataSetOST))
print("Wikimedia:", doKNN(dataSetWIK))
