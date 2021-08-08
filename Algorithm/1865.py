#1865. Finding pairs with a certain sum:
from collections import defaultdict, Counter
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freqMap1 = Counter(nums1)
        self.freqMap2 = Counter(nums2)
        for val in self.nums1:
            self.freqMap1[val] += 1
        for val in self.nums2:
            self.freqMap2[val] += 1
    #for each of the list, you may want to maintain 
    #a frequency map storing the occurrences of that
    #element
    #So here we just need to scan the frequency map
    #for the two lists.
    #after remove an element, we update the freqMap here 
    def addElement(self, index, value):
        self.freqMap2[nums2[index]] -= 1
        self.nums2[index] += value
        self.freqMap2[nums2[index]] += 1
    #finding the successful pairs:
    #just need to scan through both of the freqMap -> greatly reduce the computational costs.
    def findingPairs(self, value):
    	result = 0
        for vals in self.freqMap1.values():
            compensationValue = value - vals
            if compensationValue in self.freqMap2:
            	#product of the perspective frequency in the two frequency maps:
                result += self.freqMap1[vals] * self.freqMap2[compensationValue]
        return result

########
#so here you just need to scan the frequency map 
#for the two lists after removing an element, we update the freqMap here.
#to find the successful pairs, we just ned to scan through the freqMap
#-> worst case would also be O(n)


#AUC is classification threshold invariant.

#How to alleviate overfitting?
1. Do the regularization. -> penalize for the complexity of the model.
Force the model to be simpler
2. Perform early stopping -> 
3. Trying the ensembler, combining predictions 
from multiple separate models.

#underfitting: doesn't sufficiently utilize
#the information in the training data.

####
#A good fit in machine learning: 
#I want to select a model at the sweet spot
#between underfitting and overfitting.
####


####
#Use a resampling technique to estimate model accuracy.
#Holding back a validation dataset.

#To reduce overfitting: trying the cross-validation

#Use the initial training data to generate multiple mini train-test splits
#train with more data, remove some of the features
#Early stopping: the model's ability to 
#generalize can weaken as it begins to overfit the 
#training data.

#early stopping refers stopping the training process before the learner past the point the validation error increase again.

####

#How to detect overfitting using train-test splits?
#use feature selection


#Using the resampling technique to estimate model accuracy.
 
#Holding back a validation dataset.

#####


#holding back for a validation dataset
#-> forward stagewise additive modeling here


#merchant categories(man clothes, women jewelries, shoes)
#

#issues of using merchantID after one-hot encoding:
#making the tree skewed

#What features you can have to replace the one-hot encoding?

#using merchants related features to replace in the model?
#The size of the shop/ area of shop/ location of shops
#merchant categories, revenue of the shop
#location of the shop

#using KNN(hard threshold here): Would suggest merging the
#categories first before perform the KNN or the accuracy may not be optimal.
#check the out-of-bag accuracy of KNN?
#I would suggest using more complex models(tree-based models, ensemble models,
#xgboost, lightGBM) instead of KNN?
#For new merchant -> merging the categories before performing the KNN here.





#True failure -> slightly miss the deadline?



#merchant verification: business real? applicant real? legitimate connection
#between business and personnel?

#legality of product: product legal to sell and legal to finance?

#consumer fraud risk? will this business attract fraudsters?
#make purchases from real stores but -> different industries here.

#disputes:
#high risk for disputes?
#

#Counterparty: what's the risk this merchant will shut down within the year?
#look at a business credit report? these are similar to a 
#consumer credit report but for your business?

#claim a disputes -> when a dispute occurs, everyone loses
#The customer didn't get the item, 
#we lose a borrower here.

#This is the other side of fraud coin, instead of impersonating a
#business, fraudsters often steal a victim's payment instrument

#will be more cautious and aware when approving consumer loans for
#these businesses.

#A dispute occurs when a product is not fulfilled, arrives not as 
#described or when a return is not processed correctly.

#FICO score -> involved in the whole lifecycle of model development process?
#
#The model will decide who we lend to in real-time and 
#how we interact with our existing customers?

#work closely with credit/risk/analytics teams to understand our risk modeling
#strategy and the business drivers underlying that strategy -> for the model understanding here.

#writing production-code here and writing production-quality software
#following software engineering best practices, 
#industry engineering experience.


#Will ask for window functions as well as the dataset required.
#passion and drive to change consumer banking for the better, while
#developing a deeper understanding of applied machine learning

#willingness to learn new things, hands-on experience with python,
#spark, xgboost, airflow and aws


#only based loan approvals on one number, underwriters are missing the
#opportunity to combine modern technology and crucial data -> affect the decision here.

#look at relevant data and evolving how risk is assessed? modern underwriters 
#can approve a higher number of qualified shoppers

#can approve a higher number of qualified shoppers than a traditional FICO underwriter
#which will lead to more happy customers for you.

#which will lead to more happy customers for you?

#User, Group, Device, Photo, Status Update, Group Post, Share, IP Address etc..
#age, gender
#member count, age
#operating system
#Like count, age
#has a link?
#number of times shared?
#country, reputation -> number of accounts registered
#groups it shared to
#users commenting
#admins, group members
#entities administrated, posts etc.. -> robust to new attackers.
#most direct features can easily be changed by the person controlling the entity
#entity types considered by DEC, including user, group, device, photo,
#status update and group post




#corner case when the left-subtree and right-subtree both null?
#old and new versions of features will run in parallel universes,
#with existing models using the old universe of features with existing mo


#Use coarse rules to generate approximate labels -> low precision training by deep learning first.
#Then perform exact training

#for i in zip(*board):
#for i in zip(*board):


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        inDegree = {v: 0 for v in range(numCourses)}
        graphs = {v: [] for v in range(numCourses)}
        result = []
        SourceVertexList = []
        for i in prerequisites:
            parent, child = i[1], i[0]
            graphs[parent].append(child)
            inDegree[child] += 1
        for i in range(numCourses):
            if inDegree[i] == 0:
                SourceVertexList.append(i)
        while SourceVertexList:
            currentNode = SourceVertexList.pop()
            result.append(currentNode)
            for v in graphs[currentNode]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    SourceVertexList.append(v)
        return len(result) == numCourses
#until nothing left in the graph
    def canFinish(self, numCourses, prerequisites):
        inDegree = {v: 0 for v in range(numCourses)}
        graphs = {v: [] for v in range(numCourses)}
        result = []
        SourceVertexList = []
        for i in prerequisites:
            parent, child = i[1], i[0]
            graphs[parent].append(child)
            inDegree[child] += 1
        for i in range(numCourses):
            if inDegree[i] == 0:
                SourceVertexList.append(i)
        while SourceVertexList:
            currentNode = SourceVertexList.pop()
            result.append(currentNode)
            for v in graphs[currentNode]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    SourceVertexList.append(v)
        return len(result) == numCourses



class Graph():
    def __init__(self, nNode):
        self.graph = defaultdict(list)
        self.nNode = nNode
    def constructLink(self, u, v):
        self.graph[u].append(v)
    def topologicalSort(self):
        inDegree = {v: 0 for v in range(self.nNode)}
        SourceVertexList = []
        result = []
        for i in range(self.nNode):
            for v in self.graph[i]:
                parent, child = i, v
                inDegree[child] += 1
        for i in range(self.nNode):
            if inDegree[i] == 0:
                SourceVertexList.append(i)
        #pop one node and modify the link then finally adding the nodes with inDegree 0 unitl no 
        #node left in the array.
        while SourceVertexList:
            currentNode = SourceVertexList.pop()
            result.append(currentNode)
            for v in self.graph[currentNode]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    SourceVertexList.append(v)
        return len(result) == self.nNode







#instantly revert changes to data:
#if low-quality data is exposed to our consumers, we can 
#revert instantly to a former, consistent and correct snapshot
#of our data lake.

#writing tests:
#validity, data integrity, expected row count: 
#monitor the quality of the data is essential 
#so errors can be caught as early as possible.
#uniqueness, expected columns, expected row count

















