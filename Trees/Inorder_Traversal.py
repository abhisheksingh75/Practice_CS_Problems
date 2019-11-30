"""
Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values. Example : Given binary tree
   1
    \
     2
    /
   3
return [1,3,2]. Using recursion is not allowed.
"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def appendStack(curr, stack):
    while(curr):
        stack.append(curr)
        curr = curr.left
    return

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):

        stack = []
        ans = []
        curr = A
        appendStack(curr, stack)
        while(stack):
            ans.append(stack[-1].val)
            curr = stack.pop().right
            appendStack(curr, stack)
        return ans
            
        
        
            
            
            
            
    
