"""
Given a linked list of integers. Find and return the middle element of the linked list. Note: If there are N nodes in the linked list and N is even then return the (N/2+1)th element. 
Input Format
The only argument given head pointer of linked list.
Output Format
Return the middle element of the linked list.
Constraints
1 <= length of the linked list <= 100000
1 <= Node value <= 10^9 
For Example
Input 1:
    1->2->3->4->5
Output 1:
   3 

Input 2:
    A = 1->5->6->2->3->4
Output 2:
    2
    """
    # Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        
        slowPtr = A
        fastPtr = A
        
        while(fastPtr.next is not None and fastPtr.next.next is not None):
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        
        if fastPtr.next is not None:
            return slowPtr.next.val
        else:
            return slowPtr.val
