#1385.Find the distance value between two arrays:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        return sum(all(abs(i - j) > d for j in arr2) for i in arr1)
    #Python string manipulation, all return a boolean one.