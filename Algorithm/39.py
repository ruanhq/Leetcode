class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        def trackBack(remains, currentArray, start):
            if remains == 0:
                results.append(sorted(list(currentArray)))
                return 
            elif remains < 0:
                return
            for i in range(start, len(candidates)):
                currentArray.append(candidates[i])
                trackBack(remains - candidates[i], currentArray, i)
                currentArray.pop()
        trackBack(target, [], 0)
        return results

        