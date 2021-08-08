#716. Max Stack:

class MaxStack:
    def __init__(self):
        self.listData = []

    def pop(self) -> int:
        return self.listData.pop()

    def push(self, Element: int):
        self.listData.append(Element)

    def top(self):
        return self.listData[-1]

    def peekMax(self):
        return max(self.listData)

    def popMax(self):
        elementToPop = max(self.listData)
        for index in range(len(self.listData), -1 , -1):
            if self.listData[index] == elementToPop:
                return self.listData.pop(index)


class MaxStack:
    def __init__(self):
        self.listData = []
    def pop(self):
        return self.listData.pop()
    def push(self, Element: int):
        self.listData.append(Element)
    def top(self):
        return self.listData[-1]
    def peekMax(self):
        return max(self.listData)
    def popMax(self):
        elementToPop = max(self.listData)
        for index in range(len(self.listData), -1, -1):
            if self.listData[index] == elementToPop:
                return self.listData.pop(index)

class MaxStack:
    def __init__(self):
        self.listData = []
    

#generate dice by biased coin flip:


#generate the biased coin:
import numpy as np
def generatingUnbiasedCoinFlipping(prob):
    t1 = (np.random.random() > prob)
    t2 = (np.random.random() > prob)
    if t1 and not t2:
        return 1
    elif not t1 and t2:
        return 0
    else:
        return generatingUnbiasedCoinFlipping(prob)

def generatingDice():
    dicMapping = {[0, 0, 0]: 0,
    "001": 1,
    "010": 2,
    "011": 3,
    "100": 4,
    "101": 5,
    "110": 6}
    results = [generatingUnbiasedCoinFlipping(), 
    generatingUnbiasedCoinFlipping(), 
    generatingUnbiasedCoinFlipping()]
    if results in dicMapping.keys():
        return dicMapping[result]
    else:
        return generatingDice()

dicMap = {[0, 0, 0]: 0}


def eucDistance(X1, X2):
    return np.sqrt(np.sum((X1 - X2) ** 2))
clusters = {}
np.argmin(scipy.spatial.distance.cdist(X, centroids, 'euclidean'), axis = 1)

def recalculateClusters(X, centroids, k):
    clusters = {}
    for i in range(k):
        clusters[i] = []
    for observation in X:
        currentDist = []
        for j in range(k):
            currentDist.appe
def recalculateClusters(X, centroids, k):
	clusters = {}
    for i in range(k):
        clusters[i] = []
    for observation in X:
        eucDist = []
        for j in range(k):
            eucDist.append(eucDistance(observation, centroids[j]))
        clusters[eucDist.index(min(eucDist))].append(observation)
    return clusters

def recalculateCentroids(centroids, clusters, k):
    for i in range(k):
        centroids[i] = clusters[i].sum(axis = 0)/len(clusters[i])
    return centroids

#Generate a matrix:
X = np.random.rand(1000, 5)
k = 5
maxIter = 100
clusters = {}
for i in range(k):
    clusters[i] = []
initialAssignment = [np.random.randint(k) for _ in range(len(X))]
for i in range(len(X)):
    clusters[initialAssignment[i]].append(X[i, :])
for i in range(k):
	centroids[i] = clusters[i].sum(axis = 0)/ len(clusters[i])
for i in range(maxIter):
    currentClusters = recalculateClusters(X, centroids, k)
    if currentClusters == clusters:
        break
    centroids = recalculateCentroids(centroids, currentClusters, k)
    clusters = currentClusters

#OUTPUT them: clusters and centroids.
    
#Cumulative sum -> pick index.
#sample with weights:
def constructWeights(w):
    cumulative = []
    cdf = 0
    for weights in w:
        cdf += weights
        cumulative.append(cdf)
    return cumulative, cdf
cumulative, cdf = constructWeights(w)
target = 







    