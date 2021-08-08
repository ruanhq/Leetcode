#edit distance:
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n_1 = len(word1)
        n_2 = len(word2)
        if n_1 == 0 and n_2 == 0:
            return 0
        if n_1 == 0 and n_2 != 0:
            return n_2
        if n_1 != 0 and n_2 == 0:
            return n_1
        statesEqua = [[0] * (n_2 + 1) for _ in range(n_1 + 1)]
        if word1[0] == word2[0]:
            statesEqua[0][0] = 0
        else:
            statesEqua[0][0] = 1
        for i in range(n_1 + 1):
            statesEqua[i][0] = i
        for j in range(n_2 + 1):
            statesEqua[0][j] = j
        for i in range(1, n_1 + 1):
            for j in range(1, n_2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    statesEqua[i][j] = min(statesEqua[i - 1][j],
                    	statesEqua[i][j - 1], states[i - 1][j - 1] - 1) + 1
                else:
                    statesEqua[i][j] = min(statesEqua[i - 1][j],
                    	statesEqua[i][j - 1], statesEqua[i - 1][j - 1]) + 1
        return statesEqua[ n_1 ][ n_2 ]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n_1 = len(word1)
        n_2 = len(word2)
        if n_1 == 0 and n_2 == 0:
            return 0
        if n_1 == 0 and n_2 != 0:
            return n_2
        if n_1 != 0 and n_2 == 0:
            return n_1
        statesEqua = [[0] * (n_2 + 1) for _ in range(n_1 + 1)]
        if word1[0] == word2[0]:
            statesEqua[0][0] = 0
        else:
            statesEqua[0][0] = 1
        for i in range(n_1 + 1):


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n_1 = len(word1)
        n_2 = len(word2)
        if n_1 == 0 and n_2 == 0:
            return 0
        if n_1 == 0 and n_2 != 0:
            return n_2
        if n_1 != 0 and n_2 == 0:
            return n_1
        states = [[0] * (n_2 + 1) for _ in range(n_1 + 1)]


#Features to reduce the number of risky trips:
#exp 1000 people, 1m trip -> 350 risky trips
#con 1000 people, 1m trip -> 650 risky trips

#checkout board(收银台)

#logistic regression(random forest GBM/NN)
#what would you do if you see your model perform bad in prloduction?

#Reduce some features


#MLE position: distribute coupons, 

#Distribute the coupons, some are 0 and some are
#other digits.

#find median in 2 sorted arrays in O(logn)




class Solution:
    def findMedianSortedArray(self, nums1: List[int], nums2: List[int]) -> float:
        n_1 = len(nums1)
        n_2 = len(nums2)
        n = n_1 + n_2
        if n % 2 == 1:
            return self.kthSearch(nums1, nums2, n // 2)
        else:
            return (self.kthSearch(nums1, nums2, n // 2) +
            	self.kthSearch(nums1, nums2, n // 2 - 1)) / 2

    def kthSearch(self, A, B, k):
        n_1 = len(A)
        n_2 = len(B)
        if not A:
            return B[k]
        if not B:
            return A[k]
        i_MA = len(A) // 2
        i_MB = len(B) // 2
        A_medium = A[i_MA]
        B_medium = B[i_MB]
        if k > (i_MA + i_MB):
            if A_medium > B_medium:
                return self.kthSearch(A, B[i_MB + 1:], k - i_MB - 1)
            else:
                return self.kthSearch(A[i_MA + 1: ], B, k - i_MA - 1)
        else:
            if A_medium > B_medium:
                return self.kthSearch(A[:i_MA], B, k)
            else:
                return self.kthSearch(A, B[:i_MB], k)

#revised residuals -> improve upon the predictions 
#of the first tree, TreeI + TreeII as the prediction here.

#We then compute the classification error from this 
#new 2-tree ensemble and grow a third tree to 
#predict the revised residuals.




#What's the probability that length between x and y is not more
#than 0.5:


#The gradient boosting algorithm can be
#most easily explained by first introducing the adaboost algorithm.

#Start by training a decision tree in which each observation is
#assigned an equal weight.

#Here the idea is to improve upon the predictions on the first tree.

#CART(Classification and Regression Tree)
#weak learner: classify the data but does so poorly.

#oldTree + learningRate * NewTree -> log-odds adjustment

log(likelihood of observed data given the prediction) = (y_i * logp + (1 - y_i) * log(1 - p))
log(likelihood) * (-1)



#Using PCA to remove correlated features, imbalance, downsample, how
#to determine the downsample ratio?

#Model selection, what to do?

#trxn_id, sender_id, recerive_id, trxn_amt
How to present user engagement, count numebr of

#coding tf-idf:

sum(residual)

s1 = "SDJFgkaherofhzldskfhajklsdjhfkajldfjlkadsjfjskldjflkasdjflkjadskf"
hMap = {}
for strs in s1:
    if strs not in hMap:
        hMap[strs] = 1
    else:
        hMap[strs] += 1
dic0 = {k: v for k, v in sorted(hMap.items(), key = lambda X: X[1], reverse = True)}
list(dic0.keys())
#get 6 of them, 3 VS 3 and to test them together.
#string whether balanced?
#You may want to include a stack here.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> boolean:
        return [s.find(i) for i in s] == [t.find(i) for i in t]

from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> boolean:
        hashM1 = {}
        hashM2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if hashM1[s[i]] != hashM2[t[i]]:
                return False
            hashM1[s[i]] = i + 1
            hashM2[t[i]] = i + 1
        return True

#99% missing ratio, feature highly correlated with the target?
#What if we won't use this feature, conduct the model performance
#comparison.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> boolean:
        hashM1 = {}
        hashM2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if hashM1[s[i]] != hashM2[t[i]]:
                return False
            hashM1[s[i]] = i + 1
            hashM2[t[i]] = i + 1
        return True


#5500 - sum(array)

#Robustness: distributed over time is that even?


# G good number out of N number, randomly sample n numbers,
#the expectation value of g(g good number)


#Beacon to locate the user's ip here:



#N-Choose-k, N-Permute-k
#background, the most challenging project here.











































