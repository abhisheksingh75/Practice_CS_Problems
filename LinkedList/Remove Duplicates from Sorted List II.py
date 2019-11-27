"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. For example, Given 1->2->3->3->4->4->5, return 1->2->5. Given 1->1->1->2->3, return 2->3.
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def deleteDuplicates(self, A):
	    head = A
        tmp = head
        curr  = head
        isDuplicate = False

        if head.next is None:
            return head
        
        head = None
        curr = None        

        while(tmp.next is not None):
            
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
                isDuplicate = True
            else:
                if isDuplicate == False:
                    if head is None:
                        head = tmp
                        curr = tmp
                        #head.next = None
                    else:
                        curr.next = tmp
                        curr = curr.next
                        #curr.next = None
                        
                isDuplicate = False
                tmp = tmp.next
        if  isDuplicate ==  False:
            curr = tmp
        if curr is not None:
            curr.next = None
            
        
        return head
                        
            
            
        
