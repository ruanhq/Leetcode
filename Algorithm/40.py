#40. Combination Sum II
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates = sorted(candidates)
        self.dfsSearch(candidates, target, [], results)
        return results

    def dfsSearch(self, candidates, target, currentArray, result):
        if target == 0:
            result.append(currentArray)
            return
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            if i >= 1 and candidates[i] == candidates[i - 1]:
                continue
            self.dfsSearch(candidates[i + 1:],
            	target - candidates[i], currentArray + [candidates[i]],result)



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def trackBack(remains, currentArray, start):
            if remains == 0:
                results.append(sorted(list(currentArray)))
                return 
            elif remains < 0:
                return
            for i in range(start, len(candidates) - 1):
                currentArray.append(candidates[i])
                trackBack(remains - candidates[i], currentArray, i + 1)
                currentArray.pop()
        trackBack(target, [], 0)
        return results

class Solution:
    def combinationSum(self, candidates: List[int],)









