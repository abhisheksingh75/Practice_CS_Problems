"""
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively. Notes:
Expected solution is linear in time and constant in space.
For example,
List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
	def lPalin(self, A):
	    
        slowPtr = A
        fastPtr = A
        curr,prev,Next = None, None, None
        beg, end = None, None
        while(fastPtr.next is not None and fastPtr.next.next is not None):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        
        prev = slowPtr
        curr = prev.next
        prev.next = None
        while(curr is not None):
            #print(curr.val)
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        beg = A
        end = prev
        while(beg is not None):
            if beg.val == end.val:
                beg = beg.next
                end = end.next
                continue
            else:
                return 0
        return 1
            
            
            
            
