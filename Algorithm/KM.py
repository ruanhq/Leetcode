def recalculateClusters(X, centroids, k):
    clusters = {}
    for i in range(k):
        clusters[i] = []
    for observations in X:
        currentDist = []
        for j in range(k):
            currentDist.append(eucDistance(observations, centroids))
        clusters[currentDist.index(min(currentDist))].append(observations)
    return clusters


def recalculateCentroids(centroids, clusters, k):
    for i in range(k):
        centroids[i] = 

def recalculateClusters(X, centroids, k):
    clusters = {}
    for i in range(k):
        clusters[i] = []
    for observations in X:
        currentDist = []
        for j in range(k):
            currentDist.append(eucDistance(observations, centroids[j]))
        clusters[currentDist.index(min(currentDist))].append(observation)
    return clusters

def recalculateCentroids(centroids, clusters, k):
    for i in range(k):
        centroids[i] = [sum(t)/ len(t) for t in zip(*clusters[i])]
    return centroids

def recalculateCentroids(centroids, clusters, k):
    for i in range(k):

def recalculateClusters(X, centroids, k):
    clusters = {}
    for i in range(k):
        clusters[i] = []
    for observations in X:
        currentDist = []
        for j in range(k):
            currentDist.append(eucDistance(observations, centroids[j]))
        clusters[currentDist.index(min(currentDist))].append

centroids[i] = clusters[i].sum(axis = 0)


X = np.random.rand(1000, 5)
k = 5
clusters = {}
maxIter = 100
for i in range(k):
    clusters[i] = []
initialAssignment = [np.random.randint(k) for _ in range(len(X))]
for i in range(len(X)):
    clusters[initialAssignment[i]].append(X[i, :])
for i in range(k):
    centroids[i] = clusters[i].sum(axis = 0)/ len(clusters[i])

for i in range(maxIter):
    currentCluster = recalculateClusters(X, centroids, k)
    if currentCluster == clusters:
        break
    centroids = recalculateCentroids(centroids, currentCluster, k)
    clusters = currentCluster




#Kmeans++ avoids some of the poor clusterings.
#minimize the intra-class variance.

#pickIndex, pickIndex, pickIndex
target = self.totalSum * random.random()
low = 0
high = len(self.cumulativeSum)
while low < high:
    mid = low + (high - low) // 2
    if target > self.cumulativeSum[mid]:
        low = mid + 1
    else:
        high = mid - 1
return low

#leetcode 528:

def generatingUnbiasedCoinFlipping(prob):
    t1 = (np.random.random() > prob)
    t2 = (np.random.random() > prob)
    if t1 and not t2:
        return 1
    elif t2 and not t1:
        return 0
    else:
        return generatingUnbiasedCoinFlipping(prob)

def generatingDice(k = 6):
    dicMapping = {"000": 0,
    "001": 1,
    "010": 2,
    "011": 3,
    "100": 4,
    "101": 5,
    "110": 6}
    results = str(generatingUnbiasedCoinFlipping(0.3)) + str(generatingUnbiasedCoinFlipping(0.3)) + str(generatingUnbiasedCoinFlipping(0.3))
    if results in dicMapping.keys():
        return dicMapping[results]
    else:
        return generatingDice(k = 6)
lis2 = [generatingDice(k = 6) for _ in range(10000)]


else: return mid

def bsch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
	`
def __init__(self, w: List[int]):
    self.cumulativeSum = []
    cdf = 0
    for weight in w:
        cdf += weight
        self.cumulativeSum.append(cdf)
    self.totalSum = cdf

def pickIndex(self):
    target = self.totalSum * random.random()
    low = 0
    high = len(self.cumulativeSum)
    while low < high:
        mid = low + (high - low) // 2
        if target > self.cumulativeSum[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low

def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid



def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1


























