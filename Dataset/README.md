## PCA without standardization or normalization wtihout Log Transform
Importance of components:
                            PC1      PC2      PC3      PC4     PC5     PC6     PC7     PC8     PC9    PC10    PC11   PC12
Standard deviation     176.3247 19.90054 16.99363 12.43156 5.51085 2.63531 1.58668 0.97964 0.91324 0.75341 0.74719 0.1072
Proportion of Variance   0.9724  0.01239  0.00903  0.00483 0.00095 0.00022 0.00008 0.00003 0.00003 0.00002 0.00002 0.0000
Cumulative Proportion    0.9724  0.98480  0.99383  0.99866 0.99961 0.99983 0.99991 0.99994 0.99996 0.99998 1.00000 1.0000

## PCA after standardization and normalization and Log Transform
Importance of components:
                          PC1    PC2     PC3     PC4     PC5     PC6     PC7     PC8     PC9    PC10    PC11    PC12
Standard deviation     2.7716 1.1114 0.88127 0.84378 0.72222 0.66052 0.45092 0.42949 0.32213 0.27974 0.24444 0.08291
Proportion of Variance 0.6402 0.1029 0.06472 0.05933 0.04347 0.03636 0.01694 0.01537 0.00865 0.00652 0.00498 0.00057
Cumulative Proportion  0.6402 0.7431 0.80781 0.86714 0.91061 0.94696 0.96391 0.97928 0.98793 0.99445 0.99943 1.00000

# Correlation analysis
vcobj = varclus(~ URL+File+Lines_of_code+Require+Ensure+Include+Attribute+Hard_coded_string+Comment+Command+File_mode+SSH_KEY, data = data, trans='abs')
plot(vcobj)
thresh = 0.7
abline(h = 1 - thresh, col="grey", lty=2)

``` We remove Lines_of_code, Include, File_mode ```

# Redundancy analysis
redun_obj = redun(~ URL + File + Require + Ensure + Attribute + Hard_coded_string + Comment + Command + SSH_KEY, data=data, nk=5)

``` We remove SSH_KEY and Attribute ```

Out budget is 6

# Fitting the model

fit = lrm(defect_status ~ rcs(Hard_coded_string, 3) + URL + File + Require + Comment + Command, data = data, x=T, y=T)