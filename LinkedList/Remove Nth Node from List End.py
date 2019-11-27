"""
Given a linked list, remove the nth node from the end of list and return its head. For example, Given linked list: 1->2->3->4->5, and n = 2. After removing the second node from the end, the linked list becomes 1->2->3->5.
 Note:
If n is greater than the size of the list, remove the first node of the list.
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
        count = 0
        ptr1 = A
        ptr2 = A
        while(ptr2.next is not None and count < B):
            count += 1
            ptr2 = ptr2.next
        
        if count<B:
            A = A.next
            return A
        
        while(ptr2.next is not None):
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        ptr1.next = ptr1.next.next
        return A
	   
	    
