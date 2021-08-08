#1089. Duplicate Zeros:
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1

    #if get the 0 element, we insert a 0 here after this index
    #and pop out the right-end element here.
    #construct with a bubble sort-like solution here.


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        start = head
        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
        return start

G1 = Graph(10)
G1.constructLink(9, 3)
G1.constructLink(7, 4)



