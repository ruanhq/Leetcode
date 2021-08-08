#205. Isomorphic Strings:

class Solution(object):
    def isIsomorphic(self, s, t):
        hash1 = {}
        hash2 = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in hash2 and hash2[s[i]] != t[i]:
                return False
            if t[i] in hash1 and hash2[t[i]] != s[i]:
                return False
            hash1[s[i]] = t[i]
            hash2[t[i]] = s[i]
        return True



#To test whether two strings are isomorphic:
def isIsomorphic(self, s, t):
    d1 = [[] for _ in range(1000)]
    d2 = [[] for _ in range(1000)]
    for i, val in enumerate(s):
        d1[ord(val)].append(i)
    for i, val in enumerate(t):
        d2[ord(val)].append(i)
    return sorted(d1) == sorted(d2)


def isIsomorphic(self, s, t):
    ss1 = [s.find(i) for i in s]
    ss2 = [t.find(j) for j in t]
    return ss1 = ss2

#
map(s.find, s) == map(t.find, t)
[s.find(i) for i in s] == [t.find(j) for j in t]
len(set(zip(s, t))) == len(set(s)) == len(set(t))

def isIsomorphicMore(self, s, t):
    d1, d2 = [0 for _ in range(1000)], [0 for _ in range(1000)]
    for i in range(len(s)):
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] = i + 1
        d2[ord(t[i])] = i + 1
    return True

def isIsomorphicMore(self, s, t):
    d1, d2 = [0 for _ in range(10000)], [0 for _ in range(10000)]
    for i in range(len(s)):
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] = i + 1
        d2[ord(t[i])] = i + 1
    return True

class Solution(object):
    def depthSum(self, nestedList):
        def DFS(nestedList, depth):
            currentSum = 0
            for member in nestedList:
                if member.isInteger():
                    currentSum += member.getInteger() * depth 
                else:
                    currentSum += DFS(member.getList(), depth + 1)
            return currentSum
        return DFS(nestedList, 1)

s1 = [-1, 2, -4, 12, -25, 100]
result = [None] * len(s1)
low = 0
high = len(s1) - 1
for k in reversed(range(len(s1))):
    if s1[low] <= s1[high]:
        result[k] = s1[high]
        high -= 1
    else:
        result[k] = s1[low]
        low += 1
result



from functools import lru_cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def relation(i, j):
            if i == j:
                return 1
            elif i > j:
                return 0
            if s[i] == s[j]:
                return 2 + relation(i + 1, j - 1)
            else:
                return max(relation(i + 1, j), relation(i, j - 1))
        s1 = list(s)
        return relation(0, len(s1) - 1)



#Palindrome Substrings:
class Solution:
    def countSubstrings(self, s: str) -> int:
        low = 0
        right = len(s)
        for i in range(len(s)):
            for a, b in [(i, i), (i, i + 1)]:
                while a >= 0 and b < L and s[a] == s[b]:
                    a -= 1
                    b += 1
                r += (b - a) // 2
        return r



class Solution:
    def sortTransformedArray(self, nums: List[int],
        a: int, b: int, c: int) -> List[int]:
        nums1 = [a * x * x + b * x + c for x in nums]
        ans = [None] * len(nums1)
        lower = 0
        higher = len(nums1) - 1
        for k in reversed(range(len(ans))):
            if nums1[lower] <= nums1[higher]:
                ans[k] = nums1[high]
                high -= 1
            else:
            	ans[k] = nums1[lower]
            	lower += 1
        if a >= 0:
            return ans
        else:
            return [-x for x in reversed(ans)]


x -> [0, 1]
(y - 1)/99 = x 

yHat = 99 * x + 1
Using N(0, 1) generator to generate n data iid,
but only when x > -1:
#You may just want to do the rejection inference:

1000 tv, 1000 raters, each rater get 100 random tv
and score from (1, 10), how to do analysis:

#greadient descent: 

#Graph techniques, anomaly detection and others
#in a consumer facing product.

#What you are trying to do is to implement the
#differential expression genes.


#dimensionality reduction, clustering, regression
#classification -> expertise in
#taking projects to scale in the cloud.

#taking projects to scale in the cloud,
#ml/al based solutions and systems.
#end-to-end execution of the ml/ai solution 
#production pipeline implementation, technical recommendations
#in open source and -> hep product teams

#How did LSTM optimize over RNN:
RNN may fail to capture long dependence with long time 
where LSTM using a forget gate and an update gate here.
4 * (mn + n * n+ n): input size m, output size n.
n is the bias term, weights has n * n for each of the gate.
Gini index works better for the large partitions where cross
entropy works better for small counts but many unique values.

Explosion gradient solved by RNN: gradient clipping,
penalize the learning rate, stop backpropagating after a certain point
CART, greedy splitting, ML-use case? 
What is dropout, in the test set, it works.
Nonlinear activation fcunctions, sigmoid, tanh, relu,
leakyrelu, f(z) is 0-> asymmetric.


#generate serialization/ deserialization binary tree:

4 * (mn + n + n * n)
f(z) is 0 -> asymmetric
f(z) is 0 -> asymmetric
4 * (mn + n + n * n)


#SGD: may oscillate around the local minimum
#to prevent trapping in the local optimal(only single sample
#scan for each iteration) -> easier to fit in the memory
#may likely to reach near the minimum faster than
#(Batch) GD on large samples.

#May prone to wrong direction due to frequent updates,
#lose the benefit of vectorization since we process one
#observation per time.

#It can veer off in the wrong direction due to frequent updates.


#Which of the following is true about manhattan distance.
#distance measure do we use in case of categorical variable K-NN
#distance measure do we use in case of categorical variables KNN modeling
#here we observe that they are different.

#k-means:

#What kinds of skills we are going to extract from the linkedin?
#From people's descriptions?
#From people's skills or these?
#Features -> How to infer that people refuse to enclose all of
#their experiences?

#reservoir sampling from the stream:

def reservoirSampling(n):
	currentDict = [np.random.randint(1) for _ in range(n)]
	for i in range(n):
	    currentIndex = np.random.randint(n)
	    currentDict[currentDict] = result
	return currentDict


#What kinds of skills we are going to extract from the linkedin?
#From people's description?
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def count(i, j):
            if i == j:
                return 1
            elif i > j:
                return 0
            if s[i] == s[j]:
                return 2 + count(i + 1, j - 1)
            else:
                return max(count(i + 1, j), count(i, j - 1))
        return count(0, len(s) - 1)






#Kmeans:

for i in range(num_iter):
    gradients = X_new.T.dot(X_new.dot(theta) - Y)
    theta = theta - (1/ m) * alpha * gradients

for i in range(num_iter):
    gradients = X_new.T.dot(X_new.dot(theta) - Y)
    theta = theta - (1/ m) * alpha * gradients
h = X_new.dot(theta)
outer(a, b)
multiply(a, b)
#kmeans like this are working for vectorization here!


A1.dot(A2)
A3.dot(A4)
a = list(np.random.randint(100) for _ in range(1000))
b = list(np.random.randint(100) for _ in range(1000))
dot = 0
import time
ti = time.process_time()
for i in range(len(a)):
    dot += a[i] * b[i]
time.process_time() - ti
ti2 = time.process_time()
np.dot(a, b)
time.process_time() - ti2


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int): 
























