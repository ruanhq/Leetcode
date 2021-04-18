#1010. Pairs of songs with total duration divisible by 60:
import collections
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        result = 0
        hashMapResidual = defaultdict(int)
        for i in range(len(time)):
            if time % 60 == 0:
                result += hashMapResidual[time%60]
            else:
                result += hashMapResidual[60 - time % 60]
            hashMapResidual[time%60] += 1
        return result



class Solution(object):
    def numPairsDivisibleBy60(self, time):
        result = 0
        hashMapResidual = defaultdict(int)
        for i in range(len(time)):
            if time % 60 == 0:
                result += hashMapResidual[time % 60]
            else:
                result += hashMapResidual[60 - time % 60]
            hashMapResidual[time%60] += 1
        return result



