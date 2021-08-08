#kernelPCAAnomalyDetection:
from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
import numpy as np
import random
from sklearn.preprocessing import StandardScaler
#Write them as a class:
import warnings
class PCAObj():
    def __init__(self, nComp = 2, contamination = 0.02):
        self.nComp = nComp
        self.contamination = contamination
    def _meanCenter(self, data):
        mean =  np.repeat(np.expand_dims(np.mean(data, axis = 0), axis = 0), data.shape[0], axis = 0)
        data = data - mean
        return data
    def _fit(self, data):
        self.n_sample = len(data)
        self.CovarMatrix = (1/ self.n_sample) * data.T.dot(data)
        eigvalue, eigvecs = eigh(CovarMatrix)
        eigvalue, eigvecs = eigvalue[::-1], eigvecs[:, ::-1]
        self.eigvalue = eigvalue
        self.eigvecs = eigvecs
    def _anomalyRank(self, data):
        if data.ndim == 1:
            data = np.expand_dims(data, axis = 0)
        new_data = (self.eigvecs.T.dot(X.T)).T
        reconstructed_data = (self.eigvecs[:, :self.nComp].T.dot(X.T)).T
        self.scores = new_data.dot(new_data.T).sum(axis = 0) - reconstructed_data.dot(reconstructed_data.T).sum(axis = 0)    	
        thresholds_ = np.quantile(abs(self.scores), 1- self.contamination)
        labels = np.zeros(self.scores.shape[0])
        labels[self.scores >= thresholds_] = 1
        return labels

from scipy.spatial.distance import pdist, squareform
from scipy import exp
from scipy.linalg import eigh
import warnings
class KernelPCA():
    def __init__(self, nComp = 2, contamination = 0.03, kernel = 'rbf',
        gamma = 0.5, paramPoly = 2):
        self.nComp = nComp
        self.contamination = contamination
        self.kernel = kernel
        self.gamma = gamma
        self.paramPoly = paramPoly
    def _Standardize(self, data):
        mean = np.repeat(np.expand_dims(np.mean(data, axis = 0), axis = 0), data.shape[0], axis = 0)
        stds = np.repeat(np.expand_dims(np.std(data, axis = 0), axis = 0), data.shape[0], axis = 0)
        data = (data - mean) / stds
        return data
    def KernelMatrix(self, data):
        sqDists = pdist(data, 'sqeuclidean')
        matDistMat = squareform(sqDists)
        if self.kernel == "rbf":
            K = np.exp(- gamma * matDistMat)
        else:
            K = np.power((matDistMat + 1), 2)
        self.K = K
    def eigenEval(self):
        n = self.K.shape[0]
        oneN = np.ones((n, n)) / n
        KHat = self.K - oneN.dot(self.K) - self.K.dot(oneN) + oneN.dot(self.K).dot(oneN)
        eigvals, eigvecs = eigh(KHat)
        eigvals, eigvecs = eigvals[::-1], eigvecs[:, ::-1]
        self.eigvecs = eigvecs
        self.eigvals = eigvals
        self.dataAfterPC = np.column_stack([eigvecs[:, i] for i in range(self.nComp)])
    def _anomalyRank(self, data):
        reconstructError = np.zeros(data.shape[0])
        new_data = (self.eigvecs.T.dot(self.K.T)).T
        reconstructed_data = (self.eigvecs[:, :self.nComp].T.dot(K.T)).T
        self.scores = new_data.dot(new_data.T).sum(axis = 0) - reconstructed_data.dot(reconstructed_data.T).sum(axis = 0)    	
        thresholds_ = np.quantile(abs(self.scores), 1- self.contamination)
        labels = np.zeros(self.scores.shape[0])
        labels[self.scores >= thresholds_] = 1
        return labels





















