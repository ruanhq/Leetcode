#26. Remove Duplicates from sorted array:
class Solution(object):
    def removeDuplicatesSortedArray(self, arrays):
        if len(arrays) == 0:
            return 0
        i = j = 1
        currentCount = 1
        while j < len(arrays):
            if arrays[j] != arrays[j - 1]:
                currentCount = 1
                arrays[i] = arrays[j]
                i += 1
                j += 1
            else:
                if currentCount < 2:
                    arrays[i] = arrays[j]
                    i += 1
                    currentCount += 1
                    j += 1
                else:
                    j += 1
        return i

    

