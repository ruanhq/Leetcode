#369. Plus One linked list:
class Solution:
	def plusOne(self, head: ListNode) -> ListNode:
		first_point = ListNode(0)
		first_point.next = head
		not_nine = first_point
		while head:
			if head.val != 9:
				not_nine = head
			head = head.next
		not_nine.val += 1
		not_nine = not_nine.next
		while not_nine:
			not_nine.val = 0
			not_nine = not_nine.next
		if first_point.value > 0:
			return first_point
		else:
			return first_point.next
#Finding the rightmost non-nine digit.