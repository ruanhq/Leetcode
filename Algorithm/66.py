#66. Plus One:
class Solution(object):
    def plusOne(self, digits):
        if len(digits) == 1 and digits[-1] == 9:
            return [1, 0]
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
            return digits




class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [element for element in str(int("".join(str(t) for t in digits)) + 1)]