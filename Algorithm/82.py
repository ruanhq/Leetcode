#82 Remove Duplicates from sorted lists II
class Solution:
    def deleteDuplicates(self, head):
        sentinelNode = ListNode(0, head)
        pred = sentinelNode
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next
        return sentinelNode.next



class Solution:
    def deleteDuplicates(self, head):
        sentinelNode = List(0, head)
        pred = sentinelNode
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pred.next = head.next
            else:
                pred = pred.next
            head = head.next
        return sentinelNode.next
