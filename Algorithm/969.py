#969. Pancake sorting:
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for i in range(n, 0, -1):
            indexToChange = arr.index(i)
            if indexToChange == i - 1:
                continue
            if indexToChange != 0:
                result.append(indexToChange + 1)
                arr[:(indexToChange + 1)] = arr[:(indexToChange + 1)][::-1]
            result.append(i)
            arr[:i] = arr[:i][::-1]
        return result

#let's construct a subsequence with a defaultdict to store the values here.
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for i in range(n, 0, -1):
            indexToChange = arr.index(i)
            if indexToChange == i - 1:
                continue
            if indexToChange != 0:
                result.append(indexToChange + 1)
                arr[:(indexToChange + 1)] = arr[:(indexToChange + 1)][::-1]
            result.append(i)
            arr[:i] = arr[:i][::-1]
        return result