#46. Permutations:
class Solution(object):
    def permute(self, nums):
        result = []
        def searching(k):
            if k == len(nums):
                result.append(nums[:])
            for i in range(k, len(nums)):
                nums[i], nums[k] = nums[k], nums[i]
                searching(k + 1)
                nums[i], nums[k] = nums[k], nums[i]
        n = len(nums)
        searching(0)
        return result

#Linkedin HighFrequency Questions:
import requests

url = 'https://github.com/CapitalOneRecruiting/DS/blob/master/transactions.zip'
r = requests.get(url)
# open method to open a file on your system and write the contents    
with open("file.zip", "wb") as code:
    code.write(r.content)

#calculate the product without current number:
def productWithoutCurrent(nums):
	if len(nums) == 1:
	    return [nums[0]]
    n = len(nums)
    leftA1 = [0] * n
    rightA1 = [0] * n
    leftA1[0] = nums[0]
    rightA1[n - 1] = nums[n - 1]
    for i in range(1, n):
        leftA1[i] = leftA1[i - 1] * nums[i]
    for i in range(n - 2, -1, -1):
        rightA1[i] = rightA1[i + 1] * nums[i]
    result = [0] * n
    result[0] = rightA1[1]
    result[n - 1] = leftA1[n - 2]
    for i in range(1, n - 1):
        result[i] = leftA1[i - 1] * rightA1[i + 1]
    return result

#naive bayes:
class NaiveBayes(object):
	def __init__(self, ):

    def calculatePrior()























