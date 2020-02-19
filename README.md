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