#9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        newNumber = 0
        inputNum = x
        while x > 0:
            newNumber = newNumber * 10 + x%10
            x = x// 10
        return newNumber == inputNum

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]





#lists[startAt: endBefore: Skip]:
#lists[startAt: endBefore: Skip]:

class Solution:
    def reverseInteger(self, x: int) -> bool:
        newNumber = 0
        while x > 0:
            newNumber = newNumber * 10 + x % 10
            x = x // 10
        return newNumber



def reverseInteger(x: int) -> int:
    newNumber = 0
    while x > 0:
        newNumber = newNumber * 10 + x % 10
        x = x // 10
    return newNumber
reverseInteger(1274)


def reverseInteger(x: int) -> int:
    newNumber = 0
    while x > 0:
        newNumber = newNumber * 10 + x % 10
        x = x // 10
    return newNumber











