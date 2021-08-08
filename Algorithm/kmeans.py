
def kmeans(X, k, centroids, iterations):
    assign = np.argmax(distance.cdist(X, centroids), axis = 1)
    for _ in range(iterations):
        newCentroid = np.vstack([X[assign == i, :] for i in range(k)])
        newAssign = np.argmax(distance.cdist(X, newCentroid), axis = 1)
        if newAssign == assign:
            break
        assign = newAssign
    return assign


def knn(trainSample, testSample, k):
    dists = distance.cdist(testSample, trainSample, "euclidean")
    index = dists.argsort(axis = 1)[:, :k]
    prediction = np.mean(trainSample[index], axis = 1)
    return prediction

from scipy.spatial.distance import pdist, squareform

def knn(trainSample, k):
    pairDists = squareform(pdist(trainSample))
    index = pairDists.argsort(axis = 1)[:, 1:(k + 1)]
    prediction = np.mean(trainSample[index], axis = 1)
    return prediction


def knn(trainSample, k):
    pairDists = squareform(pdist(trainSample))
    index = pairDists.argsort(axis = 1)[:, 1 : (k + 1)]
    prediction = np.mean(trainSample[index], axis = 1)
    return prediction

def knn(trainSample, k):
    pairDists = squareform(pdist(trainSample))
    index = pairDists.argsort(axis = 1)[:, 1: (k + 1)]
    prediction = np.mean(trainSample[index], axis = 1)
    return prediction
    
#for bfs, you need to use queue.

