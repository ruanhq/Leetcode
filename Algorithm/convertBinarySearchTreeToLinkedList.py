#Convert binary search tree from the list/linked list:

#To construct a binary search tree(balanced), I would suggest using
#the 



def convertLinkedListToBST(head):
    def findMidPoint(head):
    	#dummy1 refers to the None, we need this to remove the 
    	#link between the first part of the linked list and the second part of the
    	#linked list.
        dummy1 = None
        slowP = head
        fastP = head
        while fastP and fastP.next:
            dummy1 = slowP
            slowP = slowP.next
            fastP = fastP.next.next
        if dummy1:
            dummy1.next = None
        return slowP

    if not head:
        return None
    middle = findMidPoint(head)
    node = TreeNode(middle.val)
    if head == middle:
        return node
    node.left = convertLinkedListToBST(head)
    node.right = convertLinkedListToBST(middle.next)
    return node#Here the node would be the root of the binar search tree here.


class Solution:
    def sortedListToBST(self, head):
        dummy1 = None
        slowP = head
        fastP = head
        while fastP and fastP.next:
            dummy = slowP
            slowP = slowP.next
            fastP = fastP.next.next
        if dummy1:
            dummy1.next = None
        return slowP

    def findMiddlePoint(head):
    	lengthOfList = 0
    	dummy1 = head
    	dummy2 = head
    	dummy3 = head
    	while dummy1:
    	    dummy1 = dummy1.next
    	    lengthOfList += 1
    	while index < lengthOfList//2:
    	    dummy2 = dummy2.next
    	    dummy3 = dummy3.next
    	if dummy2:
    	    dummy2.next = None
    	return dummy3





