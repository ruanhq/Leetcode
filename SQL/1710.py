#1710. Maximum units on a truck:
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda X: X[1], reverse = True)
        result = 0
        currentTruckSize = 0
        for [i, c] in boxTypes:
            if i + currentTruckSize <= truckSize:
                result += i * c
                currentTruckSize += i
            else:
                addOnThisCycle = truckSize - currentTruckSize
                result += addOnThisCycle * c
                break
        return result
        