"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
	    
        ans = []
        stack = []
        if A is None:
            return 
        else:
            stack.append(A)
        
        while(stack != []):
            curr_node = stack.pop()
            
            if curr_node.right is not None:
                stack.append(curr_node.right)
            if curr_node.left is not None:
                stack.append(curr_node.left)
            ans.append(curr_node.val)
        return ans
                
            
            
	 
