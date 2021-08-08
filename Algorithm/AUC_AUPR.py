#AUC calculation

def auc(actualPred, labelPred):
    numPositive = len([0 for x in actualPred if x == 1])
    numNegative = len(actual) - numPositive
    sumPositive = sum([r[i] for i in range(len(r)) if actualPred[i] == 1])
    auc = ((sumPositive - numPositive * (numPositive + 1)/ 2.0)/ (numNegative * numPositive))
    return auc

Why you need confusion matrix?
List regression and classification metrics, 
explain pros/cons and when to use which?
Differences between L1 and L2 regularization?
Why L-1 regularization can be used for feature selection?
Does logistic regression with squared loss function
is non-convex or convex?

How do you select lambdas ()?
What's the difference between bagging and boosting(and stacking)?'

How is amazon able to recommend other things to buy?
How does the recommendation engine work?
What is a recommendation system?
max pooling, oneVsAllAUC, oneVsAllAUC, maxPooling, 

def aucCalculation(actualPred, labelPred):
	if len(actualPred) != len(labelPred):
	    return -1
    actualPred.sort()
    labelPred.sort()
    tpr = [0] * len(actualPred)
    fpr = [0] * len(actualPred)
    auc = 0
    for i in range(1, len(labelPred)):
        currentLabel = [1 if t > labelPred[i] else 0 for t in labelPred]
        tp = np.sum(labelPred[(i + 1): ] == currentLabel[(i + 1): ])
        fp = n - i - np.sum(tp)
        tn = np.sum(labelPred[: i] == currentLabel[: i])
        fn = i - tn
        tpr[i] = fp / (fp + tn)
        fpr[i] = tp / (tp + fn)
        auc += (tpr[i] - tpr[i - 1]) * (fpr[i] + fpr[i - 1])/2
    return auc


import os
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint
from kaggle_datasets import KaggleDatasets
import transformers
from tokenizers import BertWordPieceTokenizer

with strategy.scope():
    transformer_layer = (
    	transformers.TFDistilBertModel.from_pretrained("distilbert-base-multilingual-cased"))
    model = build_model(transformer_layer, max_len = MAX_LEN)
model.summary()

v_01 = A[0, :] - A[1, :]
s_01 = get_I(v_01.dot(y[2] - y[1]) * v_01.dot(probas[2] - probas[1]))
AUC_mu = 2 / (K * (K - 1)) * (s_01 + s_02 + s_03)

class Solution:
    def flattenTree(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            return node
        leftTail = self.flattenTree(node.left)
        rightTail = self.flattenTree(node.right)
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        return rightTail if rightTail else leftTail


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 0:
            return False
        elif len(flowerbed) == 1:
            return flowerbed[0] == 0
        currentCount = 0
        newList = [0] + flowerbed + [0]
        for index in range(len(flowerbed)):
            if newList[index : (index + 3)] == [0, 0, 0]:
                currentCount += 1
        return currentCount >= n






def auROC(prediction, label):
    posCount = np.sum(label)
    negCount = len(label) - posCount
    sortedLabel = []
    for (s, t) in sorted(zip(prediction, label), reverse = True):
        sortedLabel.append(t)
    sortedPrediction = sorted(prediction, reverse = True)
    tp = fp = 0
    tprList = fprList = []
    for i in range(len(sortedLabel)):
        if sortedLabel[i] == 1:
            tp += 1
        else:
            fp += 1
        tprList.append(float(tp/posCount))
        fprList.append(float(fp/negCount))
    if tp < 1:
        return None
    pasttpr = [0] + tprList[:(len(tprList) - 1)]
    auROC = 0
    for (i, j, k) in zip(tprList, pasttpr, fprList):
        auROC += ((i - j) * k) / 2
    return auROC

def auPR(prediction, label):
    posCount = np.sum(label)
    negCount = len(label) - posCount
    sortedLabel = []
    for (s, t) in sorted(zip(prediction, label), reverse = True):
        sortedLabel.append(t)
    sortedPrediction = sorted(prediction, reverse = True)
    tp = fp = 0
    prList = rcList = []
    for i in range(len(sortedLabel)):
        if sortedLabel[i] == 1:
            tp += 1
        else:
            fp += 1
        prList.append(float(tp / (tp + fp)))
        rcList.append(float(tp / (posCount - tp)))
    if tp < 1:
        return None
    pastPR = [0] + prList[:(len(prList) - 1)]
    auPR = 0 
    for (i, j, k) in zip(prList, pastPR, rcList):
        auPR += ((i - j) * k)/ 2
    return auPR

def countBits(num: int) -> List[int]:
    result = [0]
    if num > 0:
        while len(result) < num + 1:
            result.extend([x + 1 for x in result])
    return result

def auROCPR(prediction, label):
    posCount = np.sum(label)
    negCount = len(label) - posCount
    sortedLabel = []
    for (s, t) in sorted(zip(prediction, label), reverse = True):
        sortedLabel.append(t)
    

#

def auPR(prediction, label):
    posCount = np.sum(label)
    negCount = len(label) - posCount
    sortedLabel = []
    for (s, t) in sorted(zip(prediction, label), reverse = True):
        sortedLabel.append(t)
    sortedPrediction = sorted(prediction, reverse = True)
    tp = fp = 0
    prList = rcList = []
    for i in range(len(sortedLabel)):
        if sortedLabel[i] == 1:
            tp += 1
        else:
            fp += 1
        prList.append(float(tp / (tp + fp)))
        rcList.append(float((negCount - posCount + tp)/ (negCount)))
    if tp < 1:
        return None
    pastPR = [0] + prList[:(len(prList) - 1)]
    result = 0
    for (i, j, k) in zip(prList, pastPR, rcList):
        result += ((i - j) * k)/ 2
    return result










