"""
Given a linked list of integers. Find and return the length of the longest palindrome list that exists in that linked list. Note: A palindrome list is a list that reads the same backward and forward. Expected memory complexity : O(1) 
Input Format
The only argument given is head pointer of the linked list.
Output Format
Return the length of the longest palindrome list.
Constraints
1 <= length of the linked list <= 2000
1 <= Node value <= 100 
For Example
Input 1:
    2 -> 3 -> 3 -> 3
Output 1:
   3 

Input 2:
    A = 2 -> 1 -> 2 -> 1 ->  2 -> 2 -> 1 -> 3 -> 2 -> 2
Output 2:
    5
    """
    # Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

def lenOfPalindrome(node1, node2):
    length = 0
    
    while(node1 and node2):
        if node1.val == node2.val:
            length += 2
            node1 = node1.next
            node2 = node2.next
        else:
            return length
    return length

class Solution:
    
    def solve(self, head):
        
        prev= None
        curr = head
        max_len = 0
        while(curr is not None):
            #print(curr.val)
            tmp = curr.next
            curr.next = prev 
            
            even_len = 0
            even_len = lenOfPalindrome(curr, tmp)
            
            odd_len = 0
            odd_len = lenOfPalindrome(prev, tmp) + 1
            
            max_len = max(max_len,odd_len,even_len)
            
            prev = curr
            curr = tmp
            
            
        return max_len
