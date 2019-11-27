"""
Write a program to find the node at which the intersection of two singly linked lists begins. For example, the following two linked lists:
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.
 Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Problem approach completely explained : VIDEO: https://www.youtube.com/watch?v=gE0GopCq378 Complete code in the hints section.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        
        lenA = 0
        lenB = 0
        tmp = A
        while(tmp is not None):
            tmp = tmp.next
            lenA += 1
        tmp = B
        while(tmp is not None):
            tmp = tmp.next
            lenB += 1
        
        if lenA > lenB:
            diff = lenA-lenB
            while(diff>0):
                A = A.next
                diff -= 1
        elif lenB > lenA:
            diff = lenB - lenA
            while(diff>0):
                B = B.next
                diff -= 1
        while(A is not None and B is not None):
            if A == B:
                return A
            else:
                A = A.next
                B = B.next
        return None
        
