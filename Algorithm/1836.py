#1836. Remove duplicates from an unsorted linked list:
import collections
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        currentHead = head
        freqMap = {}
        #Construct a frequency map of the element in the linked list by scanning through.
        while currentHead:
            if currentHead.val in freqMap:
                freqMap[currentHead.val] += 1
            else:
                freqMap[currentHead.val] = 1
            currentHead = currentHead.next
        result = ListNode(None)
        currentResult = result
        currentHead = head
        #Only maintain those element which has frequency 1 in the linked list:
        while currentHead:
            if freqMap[currentHead.val] == 1:
                currentResult.next = ListNode(currentHead.val)
                currentResult = currentResult.next
            currentHead = currentHead.next
        #Return the head of the newly constructed linked list:
        return result.next
    #Different methodology using defaultdict:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dicts = collections.defaultdict(int)
        currHead = head
        while currHead:
            dicts[currHead.val] += 1
            currHead = currHead.next
        dummyNode = ListNode(None)
        dummyNode = head
        previousNode = dummyNode
        while head:
            if dicts[head.val] > 1:
                previousNode.next = head.next
            else:
                previousNode = previousNode.next
            head = head.next
        return dummyNode.next



reducing size headaches: why use stride of 1 in CONV?
Why use padding?
Compromising based on memory constraints?


Bi-directional LSTM -> LSTM:
Compare with the logistic regression -> 

Took a calculated risk
Worked beyond your responsibility?
Talk about a true failure?


