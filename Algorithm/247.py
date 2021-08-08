#Strobogrammatic:s
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def helper(n):
            if n == 1:
                return ["0", "1", "8"]
            if n == 2:
                return ["00", "11", "88", "69", "96"]
            else:
                result = []
                for baseElement in helper(n - 2):
                    result.append('0' + baseElement + '0')
                    result.append('1' + baseElement + '1')
                    result.append('6' + baseElement + '9')
                    result.append('9' + baseElement + '6')
                return result
        if n == 1:
            return ["0", "1", "8"]
        if n == 2:
            return ["11", "88", "69", "96"]
        return [t for t in helper(n) if t[1] != '0' and t[-1] != '0']
        
#reduce the vanishing gradient phenomenon
#activation function for neural networks:
#