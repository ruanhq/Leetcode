#340. Longest substring with at most k distinct characters:
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int):
        result = 0
        left = 0
        i = 0
        hashMap = {}
        n = len(s)
        while i < n:
            hashMap[s[i]] = i
            i += 1
            if len(hashMap) > k:
                indexToDel = min(hashMap.values())
                del hashMap[s[indexToDel]]
                left = indexToDel + 1
            result = max(result, i - left)
        return result


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int):
        result = 0
        left = 0
        i = 0
        hashMap = {}
        n = len(s)
        while i < n:
            hashMap[s[i]] = i
            if len(hashMap) > k:
                indexToDel = min(hashMap.values())
                del hashMap[s[indexToDel]]
                left = indexToDel + 1
            result = max(result, i - left + 1)
            i += 1
        return result


    #list storing the element right and left to the current index.
    #storing the 

    #For each element in nums1: we can find the farthest element in nums2
    #that are smaller than it.

#bisect_left: insertion point in the array to maintain sorted order.

def maxDistance(self, nums1: List[int], nums2: List[int]):
    result = 0
    nums2.sort()
    for i, j in enumerate(nums1):
        l = bisect.bisect_left(nums2, j)
        if len(nums2) - l - 1 >= i:
             result = max(result, len(nums2) - 1 - l - i)
    return result


#get the BFS:
#diagram analysis, model selection, metric design,
#linear model & nonlinear model -> how to evaluate the model?



#Output the reversed input string but keep the original order of digits:

#currency_pairs = [('USD, 'CNY'),
#('JPY', 'USD'), ('CNY', 'JPY'), ('CAD', 'USD'),
#('BRL', 'USD')]
#exchange_rate = [6,95, 0.0093, 15.34, 0.75, 0.18]
#underscore split the stirng, 
def reverseStr(strs: str):
	listOfSubString = strs.split("_")
	n = len(listOfSubString)
	index = 0
	result = ""
	for i in range(n):
        if not listOfSubString[i].isdigit():
            listOfSubString[i] = listOfSubString[i][::-1]
    return "_".join(listOfSubString)
    

string = '15460'
print(string.isdigit())

during prediction(test/ validation/ after production deployment),
you want to use the capability of each and every learned neurons 
and really don't likke to skip some of them randomly.'



during prediction(test/ validation/ after production deployment),
you want to use the capability of each and every learned neurons
and really don't like to skip some of them randomly'(may not be adequate)


def reverseStr(sts: str):
    listOfSubString = strs.split("_")
    n = len(listOfSubString)
    index = 0
    result = ""
    for i in range(n):
        if not listOfSubString[i].isdigit():
            listOfSubString[i] = listOfSubString[i][::-1]
    return "_".join(listOfSubString)




#additive feature attribution methods have an 
#explanation model that is a linear function of binary
#variables: where z_prime, 

#residual network usage, attention mechanism,
#


to reverse a string:
def reverseStr(sts: str):
    listOfSubString = strs.split("_")
    n = len(listOfSubString)
    index = 0
    result = ""
    for i in range(n):
        if not listOfSubString[i].isdigit():
            listOfSubString[i] = listOfSubString[i][::-1]
    return "_".join(listOfSubString)


Transactions: transaction_id, account_id, type, amount, day.






WITH A1 AS (
SELECT account_id, MONTH(day) AS month, 
SUM(amount) AS total_income
FROM Transactions
WHERE type = 'Creditors'
GROUP BY account_id, month
ORDER BY 1, 2)

SELECT DISTINCT A.account_id
FROM Account A 
JOIN A1 


pi__x_prime(z_prime) = (M - 1) / (M Choose |z_prime|)*(|z_prime| * (M - |z_prime|)
	
Recall = True Positive/ (True Positive + False Negative)
Precision = True Positive/ (True Positive + False Positive) -> True Positive Rate(TPR)
N permute K, M choose K

#When will we reach the break-even point in terms of the mortality rate?
#Role playing -> all these 


#
#enable customers of financial institutions to perform 
#financial transactions, such as cash withdrawals, deposits,
#fund transfers or account information inquiries,
##
#at any time and without the need -> 
#Will charge users who do not use the card from the issuer to perform transactions:

#The X variable are collinear and the results show multicollinearity.

#corresponding p-value will be unstable here.
#Predict a dependent(Y) variable from two or more independent(X) variables.


personalized credit card: #model tuning and validation -> no tip, 
#customer retention -> to the predictive model whole process here.

#business sense -> for behavioral you need to prepare some case studies.

#case/ features -> what kinds of features to add? How to improve the model performance?
#What should the do to reduce the delay?

Premium card -> profit, expected users who will use
the card -> estimate the number of users who will use 
the card here.

Profits -> breakeven -> how to calculate the breakeven:

Calculate the average balance -> weighted average -> 
The reason is that encouraging the users to spend more money here.

marketing campaign -> response rate -> balance -> 
response targeted balance -> calculate the weighted average of balance
-> target those users who already have high consumer would be much more harder.


#
#
#
#
#walk through a mapreduce problem:
#Four problems: name, category, # of transactions in 2014, 
#mapper, reducer: 

#Like anagrams -> read in a string -> the word is split by the empty space, 

#How to evaluate the model performance? 
#You may want to tune the hyperparameters -> 
#improve the hyperparameters

#What if the dataset is toooooo large?

#inner bank, outer of the banks: you may need to 
#calculate the annually profits, but the ratio of 
#non-banker users -> what to consider?

















