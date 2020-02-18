# ECE611-Replication

### Data Flow
```
DataSet -> PCA -> PCA_OUT |
                          | -> Algorithm
DataSet -> +1 -> Log      |
```

### PCA without Standardazion
```
[doANN] for Mirantis is {'precision:': 0.6666666666666666, 'accuracy:': 0.6111111111111112, 'auc:': 0.659172077922078, 'recall:': 0.6666666666666666, 'f1_measure:': 0.6666666666666665}
[doCART] for Mirantis is {'precision:': 0.625, 'accuracy:': 0.6111111111111112, 'auc:': 0.5899038461538462, 'recall:': 0.6, 'f1_measure:': 0.6}
[doKNN] for Mirantis is {'precision:': 0.8660714285714286, 'accuracy:': 0.7777777777777778, 'auc:': 0.7875, 'recall:': 0.7777777777777778, 'f1_measure:': 0.7777777777777778}
[doLR] for Mirantis is {'precision:': 0.7071428571428571, 'accuracy:': 0.6666666666666666, 'auc:': 0.7012987012987013, 'recall:': 0.7142857142857143, 'f1_measure:': 0.7058823529411764}
[doNB] for Mirantis is {'precision:': 0.7777777777777778, 'accuracy:': 0.6666666666666666, 'auc:': 0.6753246753246753, 'recall:': 0.5833333333333334, 'f1_measure:': 0.6666666666666666}
[doRF] for Mirantis is {'precision:': 0.7142857142857143, 'accuracy:': 0.6666666666666666, 'auc:': 0.6625, 'recall:': 0.625, 'f1_measure:': 0.6363636363636365}
[doANN] for Mozilla is {'precision:': 0.7083333333333334, 'accuracy:': 0.7155172413793103, 'auc:': 0.7070165311092731, 'recall:': 0.6324561403508772, 'f1_measure:': 0.6666666666666666}
[doCART] for Mozilla is {'precision:': 0.7047930283224402, 'accuracy:': 0.7241379310344828, 'auc:': 0.7204301075268815, 'recall:': 0.68, 'f1_measure:': 0.6896551724137931}
[doKNN] for Mozilla is {'precision:': 0.8333333333333334, 'accuracy:': 0.7586206896551724, 'auc:': 0.740430402930403, 'recall:': 0.6978260869565217, 'f1_measure:': 0.7037037037037038}
[doLR] for Mozilla is {'precision:': 0.7272727272727273, 'accuracy:': 0.7241379310344828, 'auc:': 0.7090909090909091, 'recall:': 0.6141439205955335, 'f1_measure:': 0.6602564102564101}
[doNB] for Mozilla is {'precision:': 0.6842105263157895, 'accuracy:': 0.6724137931034483, 'auc:': 0.6668669871794872, 'recall:': 0.5217391304347826, 'f1_measure:': 0.5895390070921986}
[doRF] for Mozilla is {'precision:': 0.729020979020979, 'accuracy:': 0.7413793103448276, 'auc:': 0.7435497835497835, 'recall:': 0.6909814323607427, 'f1_measure:': 0.7058823529411765}
[doANN] for Openstack is {'precision:': 0.7361874236874237, 'accuracy:': 0.6884057971014492, 'auc:': 0.675928700499701, 'recall:': 0.7349397590361446, 'f1_measure:': 0.7339525129203806}
[doCART] for Openstack is {'precision:': 0.7078252032520325, 'accuracy:': 0.6594202898550725, 'auc:': 0.6454207164252095, 'recall:': 0.7078252032520325, 'f1_measure:': 0.7076958036661112}
[doKNN] for Openstack is {'precision:': 0.803030303030303, 'accuracy:': 0.7292513815034929, 'auc:': 0.7279879691927885, 'recall:': 0.7738095238095238, 'f1_measure:': 0.7687961755758366}
[doLR] for Openstack is {'precision:': 0.6539115646258503, 'accuracy:': 0.6231884057971014, 'auc:': 0.5962480534830051, 'recall:': 0.758098223615465, 'f1_measure:': 0.6997144022847817}
[doNB] for Openstack is {'precision:': 0.7604347826086957, 'accuracy:': 0.5869565217391305, 'auc:': 0.6209714389062776, 'recall:': 0.4233031674208145, 'f1_measure:': 0.5490280511811023}
[doRF] for Openstack is {'precision:': 0.7349397590361446, 'accuracy:': 0.6739130434782609, 'auc:': 0.6667375852616817, 'recall:': 0.706599713055954, 'f1_measure:': 0.7197560975609756}
[doANN] for Wikimedia is {'precision:': 0.6875, 'accuracy:': 0.6333333333333333, 'auc:': 0.6313988095238096, 'recall:': 0.6339712918660287, 'f1_measure:': 0.6576576576576576}
[doCART] for Wikimedia is {'precision:': 0.6666666666666666, 'accuracy:': 0.6333333333333333, 'auc:': 0.6338383838383839, 'recall:': 0.6568627450980392, 'f1_measure:': 0.6666666666666666}
[doKNN] for Wikimedia is {'precision:': 0.861904761904762, 'accuracy:': 0.7333333333333333, 'auc:': 0.7532096171802054, 'recall:': 0.7303030303030302, 'f1_measure:': 0.7333333333333334}
[doLR] for Wikimedia is {'precision:': 0.7142857142857143, 'accuracy:': 0.6896551724137931, 'auc:': 0.6862745098039216, 'recall:': 0.7142857142857143, 'f1_measure:': 0.7061900610287706}
[doNB] for Wikimedia is {'precision:': 0.75, 'accuracy:': 0.6666666666666666, 'auc:': 0.6706800144300145, 'recall:': 0.5625, 'f1_measure:': 0.6428571428571428}
[doRF] for Wikimedia is {'precision:': 0.7029411764705882, 'accuracy:': 0.6333333333333333, 'auc:': 0.6466346153846154, 'recall:': 0.625, 'f1_measure:': 0.6451612903225806}
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