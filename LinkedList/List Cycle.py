"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null. Try solving it using constant additional space. Example :
Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        
        slowPtr = A
        fastPtr = A
        
        while(fastPtr.next is not None and fastPtr.next.next is not None):
            fastPtr = fastPtr.next.next 
            slowPtr = slowPtr.next
            
            if fastPtr == slowPtr:
                break;
        
        if fastPtr != slowPtr:
            return None
        else:
            slowPtr = A
            while(slowPtr!=fastPtr):
                fastPtr = fastPtr.next
                slowPtr = slowPtr.next
        return slowPtr
            
        
        
        
                
