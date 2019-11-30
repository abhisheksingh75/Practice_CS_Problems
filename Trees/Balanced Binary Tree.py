"""
Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
 Height-balanced binary tree : is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem Example :
Input : 
          1
         / \
        2   3

Return : True or 1 

Input 2 : 
         3
        /
       2
      /
     1

Return : False or 0 
         Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
         Difference = 2 > 1. 
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
def isBalancedRec(node):
    
    if node is None:
        return [0, 1]
    else:
        leftTree = isBalancedRec(node.left)
        rightTree = isBalancedRec(node.right)
        height = abs(leftTree[0]-rightTree[0])+1
        
        if leftTree[1] == 1 and rightTree[1] == 1 and abs(leftTree[0]- rightTree[0])<=1:
            return [height, 1]
        else:
            return [height, 0]
            
def isBalancedRec2(node):
    
    if node is None:
        return 0 
    else:
        left_val = isBalancedRec2(node.left)
        right_val = isBalancedRec2(node.right)
        
        if left_val >= 0 and right_val >= 0:
            if abs(left_val-right_val) <= 1:
                return max(left_val,right_val)+1
            else:
                return -1
        else:
            return -1

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):
        return 0 if isBalancedRec2(A) < 0 else 1
    	         
	    
	  
