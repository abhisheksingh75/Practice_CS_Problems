"""
Reverse a linked list from position m to n. Do it in-place and in one-pass. For example: Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.
 Note: Given m, n satisfy the following condition: 1 ≤ m ≤ n ≤ length of list. Note 2: Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question.
 """
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        curr = A
        count = 1
        start, prev, Next = None,None,None
        mnode = None
        if A.next is None:
            return A
            
        while(count<B and curr is not None):
            count += 1
            prev = curr
            curr= curr.next
            
        start = prev
        mnode = curr
        while(count<=C and curr is not None):
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
            count += 1
        
        if start is not None:    
            start.next = prev
        else:
            start = prev
            A = prev
        mnode.next = curr
        return A
        
                
