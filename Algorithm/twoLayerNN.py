#two-layer NN
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import itertools


def hashFn(x):
    tmp = [0 for _ in range(len(x))]
    for val in x.values:
        tmp[hash(val) % N] += 1
    return pd.Series(tmp, index = cols)


def nloss(self, Yh):
    loss = (1./ self.sam) * (-np.dot(self.Y, np.log(Yh).T) -
        np.dot(1 - self.Y, np.log(1 - Yh).T))


class dlnet:
    def __init__(self, x, y):
        self.X = x
        self.Y = y 
        self.Yh = np.zeros((1, self.Y.shape[1]))
        self.L = 2
        self.dims = [9, 15, 1]
        self.param = {}
        self.ch = {}
        self.grad = {}
        self.loss = []
        self.lr = 0.005
        self.sam = self.Y.shape[1]
    #####
    def nInit(self):
        np.random.seed(42)
        self.param["W1"] = np.random.randn(self.dims[1],
        self.dims[0])/ np.sqrt(self.dims[0])
        self.param["b1"] = np.zeros((self.dims[1], 1))
        self.param["W2"] = np.random.randn(self.dims[2],
        self.dims[1])/ np.sqrt(self.dims[1])
        self.param["b2"] = np.zeros((self.dims[2], 1))
        return 
    #####
    def sigMoid(self, z):
        return 1/(1 + np.exp(-z))
    ####
    def Relu(self, z):
        return np.maximum(0, z)
    ####
    def nLoss(self, Yh):
        loss = (1. / self.sam) * (-np.dot(self.Y, np.log(Yh).T) -
        np.dot(1 - self.Y, np.log(1 - Yh).T))
        return loss
    def forward(self):
        Z1 = self.param["W1"].dot(self.X) + self.param["b1"]
        A1 = Relu(Z1)
        self.ch["Z1"], self.ch["A1"] = Z1, A1
        Z2 = self.param["W2"].dot(A1) + self.param["b2"]
        A2 = sigMoid(Z2)
        self.ch["Z2"], self.ch["A2"] = Z2, A2
        self.Yh = A2
        loss = self.nLoss(A2)
        return self.Yh, loss
    def dRelu(x):
        x[x <= 0] = 0
        x[x > 0] = 1
        return x
    def dSigmoid(x):
        s = 1/ (1 + np.exp(-x))
        dZ = s * (1 - s)
        return dZ
    def backward(self):
        dLoss_Yh = -(np.divide(self.Y, self.Yh) - np.divide(1 - self.Y, 1 - self.Yh))
        dLoss_Z2 = dLoss_Yh * dSigmoid(self.ch['Z2'])
        dLoss_A1 = np.dot(self.param["W2"].T, dLoss_Z2)
        dLoss_W2 = 1./self.ch["A1"].shape[1] * np.dot(dLoss_Z2, self.ch["A1"].T)
        dLoss_b2 = 1./self.ch["A1"].shape[1] * np.dot(dLoss_Z2, np.ones([dLoss_Z2.shape[1], 1]))
        dLoss_Z1 = dLoss_A1 * dRelu(self.ch["Z1"])
        dLoss_A0 = np.dot(self.param["W1"].T, dLoss_Z1)
        dLoss_W1 = 1./ self.X.shape[1] * np.dot(dLoss_Z1, self.X.T)
        dLoss_b1 = 1./ self.X.shape[1] * np.dot(dLoss_Z1, np.ones([dLoss_Z1.shape[1], 1]))
        self.param["W1"] = self.param["W1"] - self.lr * dLoss_W1
        self.param["b1"] = self.param["b1"] - self.lr * dLoss_b1
        self.param["W2"] = self.param["W2"] - self.lr * dLoss_W2
        self.param["b2"] = self.param["b2"] - self.lr * dLoss_b2
    def gd(self, X, Y, iters = 3000):
        np.random.seed(1)
        self.nInit()
        for i in range(iters):
            Yh, loss = self.forward()
            self.backward()
            if i % 500 == 0:
                print("Cost after iteration %i: %f" %(i, loss))
                self.loss.append(loss)
        return

nn = dlnet(x, y)
nn.lr = 0.001
nn.dims = [9, 15, 1]


#learning rate changes for each training parameter
#don't need to manually tune the learning rate
#able to train on sparse data.

#May trap at local minimum point
#weights are changed after calculating gradient on the whole dataseet,
#so if the dataset is too large than this may take years to 
#converge to the minima.
#It requires large memory to calculate gradient on the whole dataset.





#easy computation, easy to implement, easy to understand
#nesterov accelerated gradient 
#adagrad: one of the disadvantages of all the optimizers explained
#is that the learning rate is constant for all parameters for 
#each cycle, changes the learning rate.
#adam: adaptive moment estimation, 

#Adam is the best optimizers, less time and more efficiently 
#than adam is the optimizer!
#For sparse data, recommend using the optimizers with dynamic
#learning rate
#If want to use gradient descent algorithm than mini-batch
#gradient descent is the best option.


#Gradient Descent -> SGD -> Mini-Batch Gradient Descent: if the 
#dataset is too large than this may take years to converge to the 
#minima.

#Gradient Descent -> SGD -> Mini-Batch Gradient Descent

#high-variance in model parameters, may shoot even afeter achieving
#global minima.

#Trying to implement the transfer learnign, allow you to selectively
#unfreeze the last n layers of a deep neural network, leaving the 
#Learned weights frozen on the rest, overall, the feature
#is not really as useful as it first sounds.


#lstm based model -> intuition of the formula, you may
#memory cell: input, output, 
#input, output, update, forget: 4 * (n * n + m * n + n)
#######
#leadership development, 
#困难 -> solving the barrier -> 协调了多少资源 -> 协调了多少人
#more broad pipeline -> 
#machine learning engineer -> 
#困难 -> solving the barrier -> 协调了多少资源 -> 协调了多少人
#more broad pipeline -> machine learning engineer


class Solution(object):
    def distanceK(self, root, target, K):
        lookup = collections.defaultdict(lambda: (None, None))

        def dfs(node, upleft, upright):
            if not node:
                return
            if upright:
                lookup[node] = (lookup[node][0], upright)
            if upleft:
                lookup[node] = (upleft, lookup[node][1])
            if node == target:
                return
            dfs(node.left, None, node)
            dfs(node.right,node, None)
        dfs(root, None, None)


class Solution:
    def convert_into_graph(self, node, parent, g):
        if not node:
            return 
        if parent:
            g[node].append(parent)
        if node.right:
            g[node].append(node.right)
            self.convert_into_graph(node.right, node, g)
        if node.left:
            g[node].append(node.left)
            self.convert_into_graph(node.left, node, g)


class Solution:
    def convert_into_graph(self, node, parent, g):
        if not node:
            return
        if parent:
            g[node].append(parent)
        if node.right:
            g[node].append(node.right)
            self.convert_into_graph(node.right, node, g)
        if node.left:
            g[node].append(node.left)
            self.convert_into_graph(node.left, node, g)
    
    def distanceK(self, root, target, K):
        g = defaultdict(list)
        visited = set()
        result = []
        que = deque()
        self.convert_into_graph(root, None, g)
        que.append((target, 0))
        while queue:
            node, distanceCurrent = queue.popleft()
            visited.add(node)
            if distanceCurrent == K:
                result.append(node.val)
            for neighbors in g[node]:
                if neighbors not in visited:
                    queue.append((neighbors, distanceCurrent + 1))
        return result


#Calculate the distance metrics in scipy:
import numpy as np
from scipy.spatial.distance import cdist, pdist, squareform
X = np.random.randn(100, 8)
Y = np.random.randn(100, 8)

#Edit Distance:
d1 = cdist(X, Y, 'cosine')
d2 = cdist(X, Y, 'correlation')
d3 = cdist(X, Y, 'jaccard')
d4 = cdist(X, Y, 'mahalanobis', VI = None)
cdist(X, Y)





#reservoir sampling:
import random
def reservoirSampling(iterable, k):
    reservoir = []
    for i, item in enumerate(iterable):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir

reservoirSampling(range(100000), 15)

#A large reservoir: calculate the current average:
def streamAvgVar(arr, n):
    avg = 0
    var = 0
    for i in range(n):
        var = i * (var + avg)/(i + 1) + (1/i) * arr[i] ** 2 - ((avg * i + arr[i])/ (i + 1)) ** 2
        avg = (avg * i + arr[i])/ (i + 1)
    return (avg, var)

def streamVar(arr, n):
    
#moving average of stream:


#Impute using knn:

#Finding median from the stream:
from heapq import *

class MedianFinder:

    def __init__(self):
        self.small1 = []
        self.large1 = []

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        return (self.heaps[self.i][0] * self.i - self.heaps[-1][0]) / 2.0


def findMedian(self):
    return (self.heaps[self.i][0] * self.i - self.heaps[-1][0]) / 2.0

def get_iv(df, feature):
    if df[feature].dtype=='object':
        d1 = df[[k, 'flag']].fillna('-111111')
        d2 = pd.crosstab(d1[k], d1.flag).fillna(0.5)
        d2['good'] = d2[0]/d2[0].sum()
        d2['bad'] = d2[1]/d2[1].sum()
        d2['bad_ratio'] = d2[1]/(d2[0]+d2[1])
        d2['iv'] = d2.apply(lambda x: (x.good-x.bad)*np.log(x.good/x.bad),1)
    else:
        _, bins = pd.qcut(df[feature], 20, retbins=True ,duplicates='drop')
        bins[0] = float('-inf')
        bins[-1] = float('inf')
        bins = np.append(bins, -0.001)
        bins.sort()
        d1['cat'] = pd.cut(d1[k],bins)
        d2 = pd.crosstab(d1.cat, d1.flag).fillna(0.5)
        d2['good'] = d2[0]/d2[0].sum()
        d2['bad'] = d2[1]/d2[1].sum()
        d2['bad_ratio'] = d2[1]/(d2[0]+d2[1])
        d2['iv'] = d2.apply(lambda x: (x.good-x.bad)*np.log(x.good/x.bad),1)
    return round(d2.iv.sum(),4), d2

sum(abs(x - X[len(X) // 2]) for x in X)


#Explaining the Gaussian Mixture and Random Forest 
def minTotalDistance(grid):
    total = 0
    for grids in grid, zip(*grid):
        X = []
        for x, row in enumerate(grid):
            X += [x] * sum(row)
        total += sum(abs(x - X[len(X) // 2]) for x in X)
    return total 

total = 0
for grids in grid, zip(*grid):
    X = []
    for x, row in enumerate(grid):
        X += [x] * sum(row)
    total += sum(abs(x - X[len(X) // 2]) for x in X)

def minTotalDistance(grid):
    total = 0
    for grids in grid, zip(*grid):
        X = []
        for x, row in enumerate(grid):
            X += [x] * sum(row)
        total += sum(abs(x - X[len(X) // 2]) for x in X)
    return total


def minTotalDistance(grid):
    total = 0
    for grids in grid, zip(*grid):
        X = []
        for x, row in enumerate(grid):
            X += [x] * sum(row)
        total += sum(abs(x - X[len(X) // 2]) for x in X)
    return total


l1, l2 regularization intuition here:
ML design: google news recommendation system.

def minTotalDistance(grid):

m = len(grid)
n = len(grid[0])
rowIndex = [i for i in range(m) for j in range(n) if grid[i][j]]
colIndex = [j for i in range(m) for j in range(n) if grid[i][j]]
bmtRow = rowIndex[len(rowIndex) // 2]
bmtCol = colIndex[len(colIndex) // 2]
rowDistance = np.sum(abs(t - bmtRow) for t in rowIndex)
colDistance = np.sum(abs(t - bmtCol) for t in colIndex)
    return rowDistance + colDistance


def deriveMinimum(L, R, f):
    currentDistance = R - L
    while currentDistance > 1e-5:
        q1 = L + (1/ 3) * (R - L)
        q2 = L + (2/ 3) * (R - L)
        [f1, f2, f3, f4] = f(L), f(q1), f(q2), f(R)
        if f1 = max(f1, f2, f3, f4):
            L = q1
        elif f4 = max(f1, f2, f3, f4):
            R = q2
        currentDistance = R - L
    return (L + R)/ 2


def deriveMinimum(L, R, f):
    currentDistance = R - L
    while currentDistance > 1e-5:
        q1 = L + (1/ 3) * (R - L)
        q2 = L + (2/ 3) * (R - L)
        [f1, f2, f3, f4] = f(L), f(q1), f(q2), f(R)
        

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def recurseTree(current_node):
            if not current_node:
                return False
            left = recurseTree(current_node.left)
            right = recurseTree(current_node.right)
            mid = current_node == p or current_node == q
            if mid + left + right >= 2:
                result = current_node
            return mid or left or right
        recurseTree(root)
        return result

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def recurseTree(current_node):
            if not current_node:
                return False
            left = recurseTree(current_node.left)
            right = recurseTree(current_node.right)













