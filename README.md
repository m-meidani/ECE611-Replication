# ECE611-Replication

### Data Flow
```
DataSet -> +1 -> Log -> PCA -> Algorithm
```

### PCA without Standardazion
```
[doCART] for Mirantis is {'precision:': 0.6666666666666666, 'accuracy:': 0.6111111111111112, 'auc:': 0.6274350649350651, 'recall:': 0.625, 'f1_measure:': 0.6666666666666665}
[doKNN] for Mirantis is {'precision:': 0.8571428571428571, 'accuracy:': 0.7777777777777778, 'auc:': 0.7916666666666667, 'recall:': 0.8090909090909091, 'f1_measure:': 0.7913043478260868}
[doLR] for Mirantis is {'precision:': 0.75, 'accuracy:': 0.7222222222222222, 'auc:': 0.7104166666666667, 'recall:': 0.6306818181818181, 'f1_measure:': 0.7007672634271099}
[doNB] for Mirantis is {'precision:': 0.8, 'accuracy:': 0.6666666666666666, 'auc:': 0.7044955044955046, 'recall:': 0.5916666666666667, 'f1_measure:': 0.6666666666666667}
[doRF] for Mirantis is {'precision:': 0.7142857142857143, 'accuracy:': 0.6666666666666666, 'auc:': 0.6529220779220779, 'recall:': 0.625, 'f1_measure:': 0.6666666666666665}
[doCART] for Mozilla is {'precision:': 0.6818181818181818, 'accuracy:': 0.7068965517241379, 'auc:': 0.7074561403508772, 'recall:': 0.68, 'f1_measure:': 0.6723163841807911}
[doKNN] for Mozilla is {'precision:': 0.8, 'accuracy:': 0.7413793103448276, 'auc:': 0.7413793103448276, 'recall:': 0.7362318840579709, 'f1_measure:': 0.7130750605326877}
[doLR] for Mozilla is {'precision:': 0.7247474747474747, 'accuracy:': 0.6896551724137931, 'auc:': 0.661904761904762, 'recall:': 0.4654761904761905, 'f1_measure:': 0.5714285714285714}
[doNB] for Mozilla is {'precision:': 0.6818181818181818, 'accuracy:': 0.6637931034482758, 'auc:': 0.65218837535014, 'recall:': 0.49193548387096775, 'f1_measure:': 0.5714285714285714}
[doRF] for Mozilla is {'precision:': 0.6939799331103679, 'accuracy:': 0.7068965517241379, 'auc:': 0.7121635610766046, 'recall:': 0.6609195402298851, 'f1_measure:': 0.6666666666666667}
[doCART] for Openstack is {'precision:': 0.6790123456790124, 'accuracy:': 0.6281670315921176, 'auc:': 0.6134085213032582, 'recall:': 0.683899433899434, 'f1_measure:': 0.6798796441653585}
[doKNN] for Openstack is {'precision:': 0.7720779220779221, 'accuracy:': 0.7028985507246377, 'auc:': 0.6961534057449453, 'recall:': 0.7577232004942849, 'f1_measure:': 0.7423266674198772}
[doLR] for Openstack is {'precision:': 0.7034640274076893, 'accuracy:': 0.6402877697841727, 'auc:': 0.6377675910721887, 'recall:': 0.6666666666666666, 'f1_measure:': 0.6832355665328806}
[doNB] for Openstack is {'precision:': 0.7596296296296297, 'accuracy:': 0.644927536231884, 'auc:': 0.6571934887724362, 'recall:': 0.5625, 'f1_measure:': 0.6400551314673452}
[doRF] for Openstack is {'precision:': 0.6951600893521965, 'accuracy:': 0.6376811594202898, 'auc:': 0.6299246462580594, 'recall:': 0.6851456458746378, 'f1_measure:': 0.6799999999999999}
[doCART] for Wikimedia is {'precision:': 0.6470588235294118, 'accuracy:': 0.6, 'auc:': 0.606456043956044, 'recall:': 0.6282894736842105, 'f1_measure:': 0.6451612903225806}
[doKNN] for Wikimedia is {'precision:': 0.8571428571428571, 'accuracy:': 0.7666666666666667, 'auc:': 0.7650297619047619, 'recall:': 0.7633053221288515, 'f1_measure:': 0.7576887232059646}
[doLR] for Wikimedia is {'precision:': 0.75, 'accuracy:': 0.6666666666666666, 'auc:': 0.6706800144300145, 'recall:': 0.625, 'f1_measure:': 0.6666666666666666}
[doNB] for Wikimedia is {'precision:': 0.7692307692307693, 'accuracy:': 0.6666666666666666, 'auc:': 0.6741071428571428, 'recall:': 0.5714285714285714, 'f1_measure:': 0.6666666666666665}
[doRF] for Wikimedia is {'precision:': 0.6666666666666666, 'accuracy:': 0.6, 'auc:': 0.6178571428571429, 'recall:': 0.6055555555555556, 'f1_measure:': 0.6267857142857143}
```

### PCA with Standardazion
```
[doANN] for Mirantis is {'precision:': 0.6833333333333333, 'accuracy:': 0.6666666666666666, 'auc:': 0.64005994005994, 'recall:': 0.6363636363636364, 'f1_measure:': 0.6381818181818182}
[doCART] for Mirantis is {'precision:': 0.6306818181818181, 'accuracy:': 0.6111111111111112, 'auc:': 0.6038961038961039, 'recall:': 0.5555555555555556, 'f1_measure:': 0.6}
[doKNN] for Mirantis is {'precision:': 0.8660714285714286, 'accuracy:': 0.7777777777777778, 'auc:': 0.7875, 'recall:': 0.7777777777777778, 'f1_measure:': 0.7777777777777778}
[doLR] for Mirantis is {'precision:': 0.7071428571428571, 'accuracy:': 0.6666666666666666, 'auc:': 0.7012987012987013, 'recall:': 0.7142857142857143, 'f1_measure:': 0.7058823529411764}
[doNB] for Mirantis is {'precision:': 0.7777777777777778, 'accuracy:': 0.6666666666666666, 'auc:': 0.6753246753246753, 'recall:': 0.5833333333333334, 'f1_measure:': 0.6666666666666666}
[doRF] for Mirantis is {'precision:': 0.7272727272727273, 'accuracy:': 0.6666666666666666, 'auc:': 0.6721153846153847, 'recall:': 0.6201923076923077, 'f1_measure:': 0.6666666666666665}
[doANN] for Mozilla is {'precision:': 0.7, 'accuracy:': 0.7241379310344828, 'auc:': 0.7145021645021645, 'recall:': 0.6440092165898618, 'f1_measure:': 0.6666666666666666}
[doCART] for Mozilla is {'precision:': 0.6785714285714286, 'accuracy:': 0.7241379310344828, 'auc:': 0.7160162141779789, 'recall:': 0.6896551724137931, 'f1_measure:': 0.6896551724137931}
[doKNN] for Mozilla is {'precision:': 0.8333333333333334, 'accuracy:': 0.7586206896551724, 'auc:': 0.740430402930403, 'recall:': 0.6978260869565217, 'f1_measure:': 0.7037037037037038}
[doLR] for Mozilla is {'precision:': 0.7272727272727273, 'accuracy:': 0.7241379310344828, 'auc:': 0.7090909090909091, 'recall:': 0.6141439205955335, 'f1_measure:': 0.6602564102564101}
[doNB] for Mozilla is {'precision:': 0.6842105263157895, 'accuracy:': 0.6724137931034483, 'auc:': 0.6668669871794872, 'recall:': 0.5217391304347826, 'f1_measure:': 0.5895390070921986}
[doRF] for Mozilla is {'precision:': 0.732051282051282, 'accuracy:': 0.7413793103448276, 'auc:': 0.7422218406593406, 'recall:': 0.6923076923076923, 'f1_measure:': 0.7083333333333334}
[doANN] for Openstack is {'precision:': 0.7396950875211745, 'accuracy:': 0.6956521739130435, 'auc:': 0.6844157878085997, 'recall:': 0.736863711001642, 'f1_measure:': 0.7388798701298701}
[doCART] for Openstack is {'precision:': 0.7115131578947369, 'accuracy:': 0.6630434782608696, 'auc:': 0.650754607149956, 'recall:': 0.7062226391494684, 'f1_measure:': 0.7112499076058837}
[doKNN] for Openstack is {'precision:': 0.803030303030303, 'accuracy:': 0.7292513815034929, 'auc:': 0.7279879691927885, 'recall:': 0.7738095238095238, 'f1_measure:': 0.7687961755758366}
[doLR] for Openstack is {'precision:': 0.6539115646258503, 'accuracy:': 0.6231884057971014, 'auc:': 0.5962480534830051, 'recall:': 0.758098223615465, 'f1_measure:': 0.6997144022847817}
[doNB] for Openstack is {'precision:': 0.7604347826086957, 'accuracy:': 0.5869565217391305, 'auc:': 0.6209714389062776, 'recall:': 0.4233031674208145, 'f1_measure:': 0.5490280511811023}
[doRF] for Openstack is {'precision:': 0.7450855478704042, 'accuracy:': 0.6834532374100719, 'auc:': 0.6799396681749624, 'recall:': 0.7142857142857143, 'f1_measure:': 0.721007940875855}
[doANN] for Wikimedia is {'precision:': 0.6470588235294118, 'accuracy:': 0.6333333333333333, 'auc:': 0.6294642857142857, 'recall:': 0.6339712918660287, 'f1_measure:': 0.6470588235294117}
[doCART] for Wikimedia is {'precision:': 0.6666666666666666, 'accuracy:': 0.6333333333333333, 'auc:': 0.6333333333333333, 'recall:': 0.6666666666666666, 'f1_measure:': 0.6470588235294118}
[doKNN] for Wikimedia is {'precision:': 0.861904761904762, 'accuracy:': 0.7333333333333333, 'auc:': 0.7532096171802054, 'recall:': 0.7303030303030302, 'f1_measure:': 0.7333333333333334}
[doLR] for Wikimedia is {'precision:': 0.7142857142857143, 'accuracy:': 0.6896551724137931, 'auc:': 0.6862745098039216, 'recall:': 0.7142857142857143, 'f1_measure:': 0.7061900610287706}
[doNB] for Wikimedia is {'precision:': 0.75, 'accuracy:': 0.6666666666666666, 'auc:': 0.6706800144300145, 'recall:': 0.5625, 'f1_measure:': 0.6428571428571428}
[doRF] for Wikimedia is {'precision:': 0.7058823529411765, 'accuracy:': 0.6333333333333333, 'auc:': 0.6503817873303167, 'recall:': 0.6153846153846154, 'f1_measure:': 0.6451612903225806}
```
### KPCA
```
[doANN] for Mirantis is {'precision:': 0.6666666666666666, 'accuracy:': 0.6666666666666666, 'auc:': 0.638011988011988, 'recall:': 0.6363636363636364, 'f1_measure:': 0.6666666666666665}
[doCART] for Mirantis is {'precision:': 0.625, 'accuracy:': 0.6111111111111112, 'auc:': 0.61875, 'recall:': 0.6, 'f1_measure:': 0.6}
[doKNN] for Mirantis is {'precision:': 0.8660714285714286, 'accuracy:': 0.7777777777777778, 'auc:': 0.7875, 'recall:': 0.7777777777777778, 'f1_measure:': 0.7777777777777778}
[doLR] for Mirantis is {'precision:': 0.7071428571428571, 'accuracy:': 0.6666666666666666, 'auc:': 0.7012987012987013, 'recall:': 0.7142857142857143, 'f1_measure:': 0.7058823529411764}
[doNB] for Mirantis is {'precision:': 0.7777777777777778, 'accuracy:': 0.6666666666666666, 'auc:': 0.6753246753246753, 'recall:': 0.5833333333333334, 'f1_measure:': 0.6666666666666666}
[doRF] for Mirantis is {'precision:': 0.7, 'accuracy:': 0.6666666666666666, 'auc:': 0.6666666666666667, 'recall:': 0.625, 'f1_measure:': 0.6666666666666665}
[doANN] for Mozilla is {'precision:': 0.7142857142857143, 'accuracy:': 0.7241379310344828, 'auc:': 0.7119572829131653, 'recall:': 0.6475155279503106, 'f1_measure:': 0.6666666666666666}
[doCART] for Mozilla is {'precision:': 0.6933760683760684, 'accuracy:': 0.7241379310344828, 'auc:': 0.7238095238095239, 'recall:': 0.6896551724137931, 'f1_measure:': 0.6857366771159874}
[doKNN] for Mozilla is {'precision:': 0.8333333333333334, 'accuracy:': 0.7586206896551724, 'auc:': 0.740430402930403, 'recall:': 0.6978260869565217, 'f1_measure:': 0.7037037037037038}
[doLR] for Mozilla is {'precision:': 0.7272727272727273, 'accuracy:': 0.7241379310344828, 'auc:': 0.7090909090909091, 'recall:': 0.6141439205955335, 'f1_measure:': 0.6602564102564101}
[doNB] for Mozilla is {'precision:': 0.6842105263157895, 'accuracy:': 0.6724137931034483, 'auc:': 0.6668669871794872, 'recall:': 0.5217391304347826, 'f1_measure:': 0.5895390070921986}
[doRF] for Mozilla is {'precision:': 0.7391304347826086, 'accuracy:': 0.7586206896551724, 'auc:': 0.7492152295700889, 'recall:': 0.6813909774436091, 'f1_measure:': 0.7142857142857143}
[doANN] for Openstack is {'precision:': 0.7406692406692407, 'accuracy:': 0.6906474820143885, 'auc:': 0.6794587796170075, 'recall:': 0.7345584871130091, 'f1_measure:': 0.7333235326546363}
[doCART] for Openstack is {'precision:': 0.7114275414563807, 'accuracy:': 0.6594202898550725, 'auc:': 0.6513098570633573, 'recall:': 0.7023809523809523, 'f1_measure:': 0.7104512725458045}
[doKNN] for Openstack is {'precision:': 0.803030303030303, 'accuracy:': 0.7292513815034929, 'auc:': 0.7279879691927885, 'recall:': 0.7738095238095238, 'f1_measure:': 0.7687961755758366}
[doLR] for Openstack is {'precision:': 0.6539115646258503, 'accuracy:': 0.6231884057971014, 'auc:': 0.5962480534830051, 'recall:': 0.758098223615465, 'f1_measure:': 0.6997144022847817}
[doNB] for Openstack is {'precision:': 0.7604347826086957, 'accuracy:': 0.5869565217391305, 'auc:': 0.6209714389062776, 'recall:': 0.4233031674208145, 'f1_measure:': 0.5490280511811023}
[doRF] for Openstack is {'precision:': 0.746150201374082, 'accuracy:': 0.693149827963716, 'auc:': 0.6835549992176498, 'recall:': 0.7204651162790697, 'f1_measure:': 0.7320261437908497}
[doANN] for Wikimedia is {'precision:': 0.6666666666666666, 'accuracy:': 0.6333333333333333, 'auc:': 0.6333333333333333, 'recall:': 0.6339712918660287, 'f1_measure:': 0.6576576576576576}
[doCART] for Wikimedia is {'precision:': 0.6666666666666666, 'accuracy:': 0.6333333333333333, 'auc:': 0.6393321751777634, 'recall:': 0.6428571428571429, 'f1_measure:': 0.6666666666666666}
[doKNN] for Wikimedia is {'precision:': 0.861904761904762, 'accuracy:': 0.7333333333333333, 'auc:': 0.7532096171802054, 'recall:': 0.7303030303030302, 'f1_measure:': 0.7333333333333334}
[doLR] for Wikimedia is {'precision:': 0.7142857142857143, 'accuracy:': 0.6896551724137931, 'auc:': 0.6862745098039216, 'recall:': 0.7142857142857143, 'f1_measure:': 0.7061900610287706}
[doNB] for Wikimedia is {'precision:': 0.75, 'accuracy:': 0.6666666666666666, 'auc:': 0.6706800144300145, 'recall:': 0.5625, 'f1_measure:': 0.6428571428571428}
[doRF] for Wikimedia is {'precision:': 0.6899038461538461, 'accuracy:': 0.6551724137931034, 'auc:': 0.6565072182719242, 'recall:': 0.6055555555555556, 'f1_measure:': 0.6428571428571429}
```
###PCA with External data
```
[doANN] for Mirantis is {'precision:': 0.7142857142857143, 'accuracy:': 0.6666666666666666, 'auc:': 0.675, 'recall:': 0.6666666666666666, 'f1_measure:': 0.6978260869565217}
External Validity [doANN] for the model trained by Mirantis is {'external test precision:': 0.5108507268544725, 'external test accuracy:': 0.5199243746364166, 'external test auc:': 0.5199243746364166, 'external test recall:': 0.935718440954043, 'external test f1_measure:': 0.6613018219754911}
[doCART] for Mirantis is {'precision:': 0.6666666666666666, 'accuracy:': 0.6111111111111112, 'auc:': 0.6179383116883117, 'recall:': 0.6201923076923077, 'f1_measure:': 0.631578947368421}
External Validity [doCART] for the model trained by Mirantis is {'external test precision:': 0.5056228446615034, 'external test accuracy:': 0.5082897033158813, 'external test auc:': 0.5082897033158813, 'external test recall:': 0.7638161721931356, 'external test f1_measure:': 0.6088224415813576}
[doKNN] for Mirantis is {'precision:': 0.9045454545454545, 'accuracy:': 0.7777777777777778, 'auc:': 0.7875, 'recall:': 0.7777777777777778, 'f1_measure:': 0.7777777777777777}
External Validity [doKNN] for the model trained by Mirantis is {'external test precision:': 0.5203649483684525, 'external test accuracy:': 0.5363583478766725, 'external test auc:': 0.5363583478766725, 'external test recall:': 0.9278650378126818, 'external test f1_measure:': 0.6667361690297471}
[doLR] for Mirantis is {'precision:': 0.7142857142857143, 'accuracy:': 0.6666666666666666, 'auc:': 0.6948051948051949, 'recall:': 0.7207792207792207, 'f1_measure:': 0.7000000000000001}
External Validity [doLR] for the model trained by Mirantis is {'external test precision:': 0.5260036582235644, 'external test accuracy:': 0.54173938336242, 'external test auc:': 0.54173938336242, 'external test recall:': 0.8906340895869691, 'external test f1_measure:': 0.661048508265687}
[doNB] for Mirantis is {'precision:': 0.75, 'accuracy:': 0.7222222222222222, 'auc:': 0.7175324675324676, 'recall:': 0.7, 'f1_measure:': 0.7058823529411765}
External Validity [doNB] for the model trained by Mirantis is {'external test precision:': 0.5131408522367116, 'external test accuracy:': 0.5235602094240838, 'external test auc:': 0.5235602094240838, 'external test recall:': 0.9203025014543339, 'external test f1_measure:': 0.6572112316389589}
[doRF] for Mirantis is {'precision:': 0.7071428571428571, 'accuracy:': 0.6666666666666666, 'auc:': 0.670995670995671, 'recall:': 0.7, 'f1_measure:': 0.6811594202898551}
External Validity [doRF] for the model trained by Mirantis is {'external test precision:': 0.5121568526574043, 'external test accuracy:': 0.5223967422920303, 'external test auc:': 0.5223967422920301, 'external test recall:': 0.9331006399069226, 'external test f1_measure:': 0.6623228035166325}
[doSVM] for Mirantis is {'precision:': 0.7, 'accuracy:': 0.6666666666666666, 'auc:': 0.6814123376623378, 'recall:': 0.6666666666666666, 'f1_measure:': 0.6833333333333333}
External Validity [doSVM] for the model trained by Mirantis is {'external test precision:': 0.5224736429094488, 'external test accuracy:': 0.5334496800465387, 'external test auc:': 0.5334496800465387, 'external test recall:': 0.8138452588714369, 'external test f1_measure:': 0.6402285714285714}
[doKmeans] for Mirantis is {'precision:': 0.4807692307692308, 'accuracy:': 0.3888888888888889, 'auc:': 0.375, 'recall:': 0.5, 'f1_measure:': 0.49999999999999994}
External Validity [doKmeans] for the model trained by Mirantis is {'external test precision:': 0.34285714285714286, 'external test accuracy:': 0.46480511925538104, 'external test auc:': 0.46480511925538104, 'external test recall:': 0.07737056428155904, 'external test f1_measure:': 0.1260962384185133}
[doANN] for Mozilla is {'precision:': 0.709005376344086, 'accuracy:': 0.7155172413793103, 'auc:': 0.7123225732600733, 'recall:': 0.6496163682864451, 'f1_measure:': 0.6726190476190477}
External Validity [doANN] for the model trained by Mozilla is {'external test precision:': 0.5102459841238431, 'external test accuracy:': 0.5189063408958697, 'external test auc:': 0.5189063408958696, 'external test recall:': 0.9383362420011635, 'external test f1_measure:': 0.6614785815972146}
[doCART] for Mozilla is {'precision:': 0.7142857142857143, 'accuracy:': 0.7241379310344828, 'auc:': 0.725595238095238, 'recall:': 0.6909814323607427, 'f1_measure:': 0.6988372093023256}
External Validity [doCART] for the model trained by Mozilla is {'external test precision:': 0.5124137247169211, 'external test accuracy:': 0.522978475858057, 'external test auc:': 0.522978475858057, 'external test recall:': 0.9424083769633508, 'external
test f1_measure:': 0.6636259127355173}
[doKNN] for Mozilla is {'precision:': 0.85, 'accuracy:': 0.7586206896551724, 'auc:': 0.7521571260701696, 'recall:': 0.7142857142857143, 'f1_measure:': 0.7126984126984126}
External Validity [doKNN] for the model trained by Mozilla is {'external test precision:': 0.5109039201789649, 'external test accuracy:': 0.5200698080279232, 'external test auc:': 0.5200698080279232, 'external test recall:': 0.9400814426992438, 'external test f1_measure:': 0.6620251864157893}
[doLR] for Mozilla is {'precision:': 0.6926536731634183, 'accuracy:': 0.6896551724137931, 'auc:': 0.6840971830102264, 'recall:': 0.5917508417508417, 'f1_measure:': 0.6391489361702127}
External Validity [doLR] for the model trained by Mozilla is {'external test precision:': 0.5074395536267824, 'external test accuracy:': 0.5139616055846422, 'external test auc:': 0.5139616055846422, 'external test recall:': 0.9522978475858057, 'external
test f1_measure:': 0.6618122977346279}
[doNB] for Mozilla is {'precision:': 0.6666666666666666, 'accuracy:': 0.6896551724137931, 'auc:': 0.6709415584415583, 'recall:': 0.5769230769230769, 'f1_measure:': 0.6116780045351475}
External Validity [doNB] for the model trained by Mozilla is {'external test precision:': 0.5040118870728083, 'external test accuracy:': 0.5078534031413613, 'external test auc:': 0.5078534031413613, 'external test recall:': 0.9866201279813845, 'external
test f1_measure:': 0.6674537583628491}
[doRF] for Mozilla is {'precision:': 0.75, 'accuracy:': 0.7758620689655172, 'auc:': 0.7668269230769231, 'recall:': 0.7142857142857143, 'f1_measure:': 0.7325203252032519}
External Validity [doRF] for the model trained by Mozilla is {'external test precision:': 0.5066811690727739, 'external test accuracy:': 0.5125072716695753, 'external test auc:': 0.5125072716695753, 'external test recall:': 0.9488074461896452, 'external
test f1_measure:': 0.6607179071182316}
[doSVM] for Mozilla is {'precision:': 0.6956521739130435, 'accuracy:': 0.6896551724137931, 'auc:': 0.6788289835164836, 'recall:': 0.5666666666666667, 'f1_measure:': 0.6153846153846153}
External Validity [doSVM] for the model trained by Mozilla is {'external test precision:': 0.5072281771028562, 'external test accuracy:': 0.5135253054101221, 'external test auc:': 0.5135253054101222, 'external test recall:': 0.9499709133216987, 'external test f1_measure:': 0.66140457397288}
[doKmeans] for Mozilla is {'precision:': 0.5684615384615385, 'accuracy:': 0.6120689655172413, 'auc:': 0.6055555555555554, 'recall:': 0.5180645161290323, 'f1_measure:': 0.527046783625731}
External Validity [doKmeans] for the model trained by Mozilla is {'external test precision:': 0.5128651302618152, 'external test accuracy:': 0.5235602094240838, 'external test auc:': 0.5235602094240838, 'external test recall:': 0.93717277486911, 'external test f1_measure:': 0.6639192252215125}
[doANN] for Openstack is {'precision:': 0.7410976120653541, 'accuracy:': 0.693149827963716, 'auc:': 0.6778846153846154, 'recall:': 0.7419247419247419, 'f1_measure:': 0.7384743706399757}
External Validity [doANN] for the model trained by Openstack is {'external test precision:': 0.5066394908612364, 'external test accuracy:': 0.5125072716695753, 'external test auc:': 0.5125072716695753, 'external test recall:': 0.9796393251890634, 'external test f1_measure:': 0.667331075297495}
[doCART] for Openstack is {'precision:': 0.7056060606060606, 'accuracy:': 0.6594202898550725, 'auc:': 0.6475678733031673, 'recall:': 0.7109772423025436, 'f1_measure:': 0.7040792540792541}
External Validity [doCART] for the model trained by Openstack is {'external test precision:': 0.5062208548596197, 'external test accuracy:': 0.5116346713205352, 'external test auc:': 0.5116346713205352, 'external test recall:': 0.9476439790575916, 'external test f1_measure:': 0.6598314050976648}
[doKNN] for Openstack is {'precision:': 0.8091736694677871, 'accuracy:': 0.7220310707955375, 'auc:': 0.7238575834034202, 'recall:': 0.7622023809523809, 'f1_measure:': 0.7613204791118902}
External Validity [doKNN] for the model trained by Openstack is {'external test precision:': 0.5072749324659573, 'external test accuracy:': 0.5139616055846422, 'external test auc:': 0.5139616055846423, 'external test recall:': 0.9738219895287958, 'external test f1_measure:': 0.6670652715852012}
[doLR] for Openstack is {'precision:': 0.6594575637128828, 'accuracy:': 0.6304347826086957, 'auc:': 0.6026658995013425, 'recall:': 0.7558139534883721, 'f1_measure:': 0.7075911208550287}
External Validity [doLR] for the model trained by Openstack is {'external test precision:': 0.5110587211221593, 'external test accuracy:': 0.5205061082024434, 'external test auc:': 0.5205061082024433, 'external test recall:': 0.9461896451425247, 'external test f1_measure:': 0.6634046878725215}
[doNB] for Openstack is {'precision:': 0.7348345588235294, 'accuracy:': 0.6521739130434783, 'auc:': 0.6554537516610015, 'recall:': 0.6453929539295393, 'f1_measure:': 0.6849315068493151}
External Validity [doNB] for the model trained by Openstack is {'external test precision:': 0.5023612750885478, 'external test accuracy:': 0.504653868528214, 'external test auc:': 0.5046538685282141, 'external test recall:': 0.9901105293775451, 'external test f1_measure:': 0.666536126884668}
[doRF] for Openstack is {'precision:': 0.7283279656468062, 'accuracy:': 0.697841726618705, 'auc:': 0.6848148148148148, 'recall:': 0.7810485001401739, 'f1_measure:': 0.7522667665792431}
External Validity [doRF] for the model trained by Openstack is {'external test precision:': 0.5038110043028098, 'external test accuracy:': 0.5072716695753345, 'external test auc:': 0.5072716695753344, 'external test recall:': 0.9575334496800465, 'external test f1_measure:': 0.660060174981034}
[doSVM] for Openstack is {'precision:': 0.6666666666666666, 'accuracy:': 0.6376811594202898, 'auc:': 0.6100634837640035, 'recall:': 0.7697968795996468, 'f1_measure:': 0.7085714285714286}
External Validity [doSVM] for the model trained by Openstack is {'external test precision:': 0.5076063334368208, 'external test accuracy:': 0.5142524723676556, 'external test auc:': 0.5142524723676556, 'external test recall:': 0.9505526468877254, 'external test f1_measure:': 0.6618049220670663}
[doKmeans] for Openstack is {'precision:': 0.5045454545454545, 'accuracy:': 0.4172661870503597, 'auc:': 0.44086621161235406, 'recall:': 0.3291911083667799, 'f1_measure:': 0.3914563697172393}
External Validity [doKmeans] for the model trained by Openstack is {'external test precision:': 0.3992673992673993, 'external test accuracy:': 0.4840023269342641, 'external test auc:': 0.48400232693426415, 'external test recall:': 0.06340895869691682, 'external test f1_measure:': 0.10943775100401608}
[doANN] for Wikimedia is {'precision:': 0.6666666666666666, 'accuracy:': 0.6333333333333333, 'auc:': 0.6333333333333333, 'recall:': 0.625, 'f1_measure:': 0.6451612903225806}
External Validity [doANN] for the model trained by Wikimedia is {'external test precision:': 0.5082145268626049, 'external test accuracy:': 0.5154159394997091, 'external test auc:': 0.5154159394997091, 'external test recall:': 0.9499709133216987, 'external test f1_measure:': 0.6619845282265523}
[doCART] for Wikimedia is {'precision:': 0.6666666666666666, 'accuracy:': 0.6333333333333333, 'auc:': 0.6416205322455323, 'recall:': 0.6449579831932774, 'f1_measure:': 0.6666666666666666}
External Validity [doCART] for the model trained by Wikimedia is {'external test precision:': 0.5063174713969948, 'external test accuracy:': 0.5117801047120418, 'external test auc:': 0.5117801047120418, 'external test recall:': 0.9537521815008726, 'external test f1_measure:': 0.6612789126087406}
[doKNN] for Wikimedia is {'precision:': 0.8461538461538461, 'accuracy:': 0.7333333333333333, 'auc:': 0.7438204887218045, 'recall:': 0.7142857142857143, 'f1_measure:': 0.7211111111111113}
External Validity [doKNN] for the model trained by Wikimedia is {'external test precision:': 0.5076205405676297, 'external test accuracy:': 0.5142524723676556, 'external test auc:': 0.5142524723676556, 'external test recall:': 0.9528795811518325, 'external test f1_measure:': 0.662344240305843}
[doLR] for Wikimedia is {'precision:': 0.7058823529411765, 'accuracy:': 0.6896551724137931, 'auc:': 0.6899350649350651, 'recall:': 0.7142857142857143, 'f1_measure:': 0.7096774193548386}
External Validity [doLR] for the model trained by Wikimedia is {'external test precision:': 0.5066604868598811, 'external test accuracy:': 0.5125072716695753, 'external test auc:': 0.5125072716695753, 'external test recall:': 0.9493891797556719, 'external test f1_measure:': 0.6610151511262823}
[doNB] for Wikimedia is {'precision:': 0.75, 'accuracy:': 0.6896551724137931, 'auc:': 0.693204365079365, 'recall:': 0.6666666666666666, 'f1_measure:': 0.6939799331103679}
External Validity [doNB] for the model trained by Wikimedia is {'external test precision:': 0.5013554247609975, 'external test accuracy:': 0.5026178010471204, 'external test auc:': 0.5026178010471204, 'external test recall:': 0.964805119255381, 'external test f1_measure:': 0.6596253487445197}
[doRF] for Wikimedia is {'precision:': 0.6666666666666666, 'accuracy:': 0.6333333333333333, 'auc:': 0.6336309523809524, 'recall:': 0.6875, 'f1_measure:': 0.6666666666666667}
External Validity [doRF] for the model trained by Wikimedia is {'external test precision:': 0.5033314133513347, 'external test accuracy:': 0.5063990692262944, 'external test auc:': 0.5063990692262944, 'external test recall:': 0.9674229203025014, 'external test f1_measure:': 0.6619268214493038}
[doSVM] for Wikimedia is {'precision:': 0.6961538461538461, 'accuracy:': 0.6896551724137931, 'auc:': 0.6889995421245422, 'recall:': 0.6990950226244343, 'f1_measure:': 0.7042925278219396}
External Validity [doSVM] for the model trained by Wikimedia is {'external test precision:': 0.5068681342242892, 'external test accuracy:': 0.5129435718440953, 'external test auc:': 0.5129435718440953, 'external test recall:': 0.9525887143688191, 'external test f1_measure:': 0.6613949696634459}
[doKmeans] for Wikimedia is {'precision:': 0.6666666666666666, 'accuracy:': 0.6, 'auc:': 0.6126217532467532, 'recall:': 0.5358974358974359, 'f1_measure:': 0.5760368663594471}
External Validity [doKmeans] for the model trained by Wikimedia is {'external test precision:': 0.5136087095741274, 'external test accuracy:': 0.5247236765561373, 'external test auc:': 0.5247236765561373, 'external test recall:': 0.9331006399069226, 'external test f1_measure:': 0.6626730014459823}
```