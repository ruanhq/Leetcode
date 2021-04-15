#1424. Diagonal Traverse II:
from collections import defaultdict
class Solution(object):
    def findDiagonalOrder(self, nums):
        dictList = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                dictList[i + j].append(nums[i][j])
        result = [v for k in dictList.keys() for v in reversed(dictList[k])]
        return result



#Sort by the first element of the value:
{k: v for k, v in sorted(dictList.items(), key = lambda X: X[1], reverse = True)}
#Sort by key:
from operator import itemgetter
#Sort by the key: itemgetter(0), Sort by the key: itemgetter(1)
sorted(dictList.items(), key = itemgetter(0), reverse = True)

sorted(dictList.items(), key = itemgetter(1), reverse = True)

sorted(dictList.items(), key = itemgetter(0), reverse = True)

#Construct a tree data structure:

#larger space/ perspective for the credit
#-> banking industry would be 
#credit-based results



def reconstructedProbability(X, LTimes = 500):
    reconstructedProbability = np.zeros((X.shape[0], X.shape[1]), dtype = 'float32')
    mu_hat, sigma_hat = 

