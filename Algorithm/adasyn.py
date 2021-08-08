#Implement the Adasyn algorithm:
from scipy.spatial.distance import cdist, pdist, squareform
import numpy as np
import pandas as pd
graph = {v: [] for v in range(numCourses)}
inDegree = {v: 0 for v in range(numCourses)}
#https://1o24bbs.com/t/topic/12345

#[2, 4, 6, 8, 10]
#i * i, i * (i + 1), ..., n: range(i ** 2, n, i)
#[i * i, i * (i + 1), ..., n: range(i ** 2, n, i)]
#
class adasyn():
    def __init__(ratio = 0.25, K = 50):
        self.ratio = ratio
        self.K = K
    #FillingOut the
    def preprocessing(self, X):
        #Impute the missing value with median:
        X = X.fillna(X.median())
        #X is the input dataframe
        #Split the categorical features and numerical features:
        categoricalFeatureList = X.select_dtypes(include = [np.object])
        numericalFeatureList = X.select_dtypes(include = [np.number])
        NumericalFeatureScaled = StandardScaler().fit_transform(X[numericalFeatureList])
        featureListNew = numericalFeatureList + categoricalFeatureList
        XNew = np.concatenate((NumericalFeatureScaled, X[categoricalFeatureList]), axis = 1)
        return XNew
    #X is the training observations
    #y is the training labels, np.array with 0 and 1 where 0 is negative label and 1 is positive label.
    def constructWeights(self, X, y):
        nMajority = len(y[y == 0])
        nMinority = len(y[y == 1])
        imbalanceRatio = len(y[y == 0])/ len(y[y == 1])
        nOverSampled = imbalanceRatio * self.ratio
        distanceGraph = squareform(pdist(X))
        KNNIndexGraph = np.argsort(distanceGraph, axis = 1)[:, 1: (self.K + 1)]
        #Construct weights for the sampling:
        Weights = np.zeros([nMinority])
        #Get the weights for the resampling:
        WeightsResample = np.apply_along_axis(lambda X: np.sum(y[X]), 1, KNNIndexGraph)
        WeightsNormalized = WeightsResample/ np.sum(WeightsResample)
    #SMOTE_NC for euclidean distance computation:
    def ncCalculation(self, X, y):
        nMajority = len(y[y == 0])
        nMinotiry = len(y[y == 1])



    #calculate Euclidean Distance:




#How to classify a email: whether it is from the company or from the public?
#Your program -> making it the
#Own the model -> engineering features ->  build the detection algorithm here
#smoteNC how did it make sense????
#
#relevant work experience: we value your experience to build model and 
#own a model

#relevant work experience: 
#production flows -> on one of the most timely & 
#challenging problems in this era.
#challenging problems in the area -> technical experience
#1+ years of relevant work experience
#MS or PhD in Computer Science or related technical discipline


#Fast-changing attacks -> dynamic attack -> extracted 
#features can bring significant robustness

#anomalous patterns -> more robust features
#with well-preserved automation behavior,
#which improves defense resilience again
#fast-changing attack signals

########
#Due to the lightweight computation, the 
#extracted signatures can be used directly 
#as the label to defend against large-scale
#attachs and provide fast defense turnaround.
########

########
#bring significant improvement in response time 
#and defense coverage on sudden and new abuse
#attacks
########
#High resilience and robustness
#behavior analytic computation -> bot-driven attacks
#without collecting extra user data
#


#Own the model in scale, nefarious activities
#cyber threat analysts as part of 
#a cross-functional team

#owning/ building detection algorithms -> leverage the 
#latest techniques to build and design solutions!


#####
#experience owning models -> writing production code 
#-> writing production code 

#Experience in building machine learning model for 
#fraud detection, writing production code and own the machine learning model


#Building the model from scratch -> to evolving -> 
#design the periodically refresh mechanism to 
#cope with the ever-evolving fraud

#Deep learning, especially graph-based modeling/ clustering

#To learn: to design the scope and the solution

#actively seeking for new challenges -> in the progress
#of phone screen like this -> I would prefer linkedin
#The solution would give me an unprecendented chance to ownly
#design/ build solutions to stay ahead of ever-evolving 
#attacker strategies.

#Knowledge of deep learning -> course project and 
#side projects -> variational autoencoders and other
#deep learning strategies


#Knowledge of deep learning -> extensive project experience -> working on deep learning strategies

#Design the periodically refresh mechanism to 
#work with the ever-evolving fraud

#write production code and own the machine learning model -> working on deep learning strategies
#actively seeking for new challenges -> in the progress
#of phone screen like this -> I would prefer linkedin 



















































