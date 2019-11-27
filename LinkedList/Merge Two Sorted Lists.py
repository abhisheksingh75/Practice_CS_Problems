"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists, and should also be sorted. For example, given following linked lists :
  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :
4 -> 5 -> 8 -> 11 -> 15 -> 20
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
	   
        Head = None
        C = None
        
        if (A.val < B.val):
            Head = A
            C = A
            A = A.next
        else:
            Head = B
            C = B
            B = B.next
        
        while(A is not None and B is not None):
	       
            if (A.val < B.val):
                C.next = A
                C = A
                A = A.next
            else:
                C.next = B
                C = B
                B = B.next
                
        while(A is not None):
            C.next = A
            C = A
            A = A.next
        while(B is not None):
            C.next = B
            C = B
            B = B.next
            
	       
        return Head# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
	   
        Head = None
        C = None
        
        if (A.val < B.val):
            Head = A
            C = A
            A = A.next
        else:
            Head = B
            C = B
            B = B.next
        
        while(A is not None and B is not None):
	       
            if (A.val < B.val):
                C.next = A
                C = A
                A = A.next
            else:
                C.next = B
                C = B
                B = B.next
                
        while(A is not None):
            C.next = A
            C = A
            A = A.next
        while(B is not None):
            C.next = B
            C = B
            B = B.next
            
	       
        return Head
