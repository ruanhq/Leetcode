#topK problems: sort/heap/quickselect:

#O(N*logN)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse = True)[k - 1]

#O(N* logK): heap -> start with empty heap, push items into it


#quick-select:



#Why lstm works better than the RNN: utilize the forget gate/ update gate to help capture the long dependence.
#cell, forget gate to control the -> 4 * (mn + n ^ 2)

#what if the conversion rate real is 2% but the model predicts the conversion rate as 20%
#inflation ->  selection bias of the sample selection

#evaluate the pros and cons of increasing the radius of merchant selection
#increase the radius of merchant selection:


#show merchants <= 5 miles -> what's the kpi ->


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s is None:
            return 0
        def searching(S: string) -> int:
            if len(S) > 0:
                if S[0] == "0":
                    return 0
            if len(S) == 1 or S == "":
                return 1
            if int(S[:2]) <= 26:
                a1 = searching(S[1:])
                a2 = searching(S[2:])
                return a1 + a2
            else:
                return searching(S[1:])
        return searching(s)



class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s is None:
            return 0
        def searching(S: string) -> int:
            if len(S) > 0:
                if S[0] == "0":
                    return 0
            if len(S) == 1 or S == "":
                return 1
            if int(S[:2]) <= 26:
            	a1 = searching(S[1:])
            	a2 = searching(S[2:])
            	return a1 + a2
            else:
                return searching(S[1:])
        return searching(s)

    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s is None:
            return 0
        def searching(S: string) -> int:
            if len(S) > 0:
                if S[0] == "0":
                    return 0
            if len(S) == 1 or S == "":
                return 1
            if int(S[:2]) <= 26:
                a1 = searching(S[1:])
                a2 = searching(S[2:])
                return a1 + a2
            else:
                return searching(S[1:])
        return searching(s)
    ######################################


#follow up on experimental design:
roll out the change in one market: how would you choose the market and 
how would you measure the success?


#conversion rate -> better customer experience, long term retention rate 
#increase exposure, acquire new users who were previously out of their reach, increase revenue.
#increase the orders -> fulfillment speed, quality drops -> rating/ customer repeat

#revenue per searcher -> what would be the secondary metrics here?




###########
##From three perspective:
#for customers -> conversion rate, better customer experience, long retention rate -> 
#longer to deliver -> impact on user experience

#for merchants: increase exposure, acquire new users who were previously out of reach -> 
#increase revenue -> fulfillment amount/ quality -> rating, customer loyalty drop
#dasher: increase the order count, but longer on road -> on-time delivery/ fulfill order drops -> revenue not necessarily increase

#What metrics -> net revenue per searcher(directly related to the kpi object here)
#what market: what objective -> how to get the market with maximum profit

#results is good, what to do? ship experience in same category market, 
#explore the different value slightly larger than 10 miles etc.
#improve merchant selection: search volume, # of the merchants in the range like this.

#measure the -> different conditions -> fall in different range of the data -> construct the confidence interval of the statistics of both group of points and aggregate them together.

#P(A | x) = P(x | A) * P(A) / (constant)
#P(x | A): fit the distribution and then calculate the posterior distribution

#P(A) + P(B) = 1
#P(A) = len(A) / (len(A) + len(B))

#P(A) = len(A) / (len(A) + len(B))

#P(A | B) = P(B | A) * P(A)/ P(B)
#proportional to length of the array: the difference is in the conditions 
#of the datasets

#present the data into the datasets:
#bagging vs boosting: 
#cross-validation
#give seasonality example, come up with features you need:
#average -> peak order count/ average order count

#retail stores -> 711 increase the profit -> 

#What would be the effect of this?


#what metrics -> net revenue per searcher(directly related to the kpi object here)
#what market: what objective -> how to get the market with maximum profit

#merchants, fulfillment amount/ quantity
#dasher -> order count, longer on road, on-time delivery/ fulfillment order ratio/percentage drops

#on-


#valid triangle number:

nums = [2, 2, 3, 4]
2, 3, 4
#python read in the data into file here:




for i in range(L - 2):
    k = i + 2
    for j in range(i + 1, L - 1):
        M = nums[i] + nums[j] - 1
        if M < nums[j]: continue
        k = bisect.bisect_right(nums, M, k)
        result += min(k, len(nums)) - j - 1
return result


nums.sort()
nums.reverse()
result = 0
n = len(nums)
for i in range(n - 2):
    j, k = i + 1, n - 1
    while j < k:
        if nums[j] + nums[k] > nums[i]:
            count += k - j
            j += 1
        else:
            k -= 1 
return count


#What variables to include? what to get? interaction plot, regression plot.














