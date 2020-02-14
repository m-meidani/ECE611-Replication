from CART.docart import doCART
from LR.dolr import doLR
from KNN.doknn import doKNN
from PCA.doPCA import applyPCA
import warnings
warnings.filterwarnings('ignore')

<<<<<<< HEAD
=======
from PCA.doPCA import applyPCA
from KNN.doknn import doKNN
from LR.dolr import doLR
from NaiveBayes.NB import doNB
from RandomForests.RF import doRF

>>>>>>> 895268cde575402be448748b6092a4e16bad490b

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
<<<<<<< HEAD
# -------------KNN
print("")
print("#------------KNN Result:")
print("Mirantis:", doKNN(dataSetMIR))
print("Mozilla:", doKNN(dataSetMOZ))
print("Openstack:", doKNN(dataSetOST))
print("Wikimedia:", doKNN(dataSetWIK))
=======

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
>>>>>>> 895268cde575402be448748b6092a4e16bad490b
