#The order would be different for training data
#and testing data, how would you make to minimize the 
#model error?

def longestPalindromeSubstring(strs):
    def countbetween(strs, i, j):
        if i == j:
            return 1
        elif i > j:
            return 0
        if s[i] == s[j]:
            return 2 + countbetween(strs, i + 1, j - 1)
        else:
            counts = max(countbetween(strs, i + 1, j), countbetween(strs, i, j - 1))
    result = countbetween(strs, 0, len(strs))
    return result



####
#we found people are spending less time in google search
#engine, why? 
#x: time on search until we find the answer ~ log-normal distribution/ geometric distribution
#time on search until 

#The length is 1, x, y randomly on each of the side ->
#What's the probability that length between x and y is 
#less than 0.5:



########
#How to deal with multicollinearity? ridge regression, 
#change to tree-based model, principal component analysis
#Partial least squares, partial least squares,
#principal components analysis
########


#features, sample size relationship; what metrics to use
#in the test?
#How to check whether it violates the hypothesis,
#Double the data and re-fit the model?

#Simulation methodology, -> rejection sampling?
#hypothesis testing



#Precision: True Positive/(True Positive + False Positive)
#Recall: True Negative/(True Negative + False Negative)
#Precision-recall curve

#ROC-CURVE to draw the plots here:
#Specificity: FPR(False-Positive/(False-Positive + True Negative))
#Sensitivity: TPR(True-Positive/(True-Positive + Fals Negative))


precision: TP/(TP + FP)
recall: TN/(TN + FN)

def fairCoin():
    coin1 = 0
    coin2 = 0
    while coin1 == coin2:
        coin1 = unfairCoin()
        coin2 = unfairCoin()
    return coin1


def generateRandom()






























