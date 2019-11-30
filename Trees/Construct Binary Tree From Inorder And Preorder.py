"""
Given preorder and inorder traversal of a tree, construct the binary tree.
 Note: You may assume that duplicates do not exist in the tree. 
Example :
Input :
        Preorder : [1, 2, 3]
        Inorder  : [2, 1, 3]

Return :
            1
           / \
          2   3
"""
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def buildTreeRec(preOrder,DicInOrder, start, end):

    if start == end :
        #create tree node
        root = TreeNode(preOrder[buildTreeRec.preIndx])
        buildTreeRec.preIndx += 1
        return root
    
    if start < end:
        
        #create tree node
        root = TreeNode(preOrder[buildTreeRec.preIndx])
        buildTreeRec.preIndx += 1
        
        #find pos of root of sub tree
        pos = DicInOrder[root.val]
        
        #repeat process for left subtree
        root.left = buildTreeRec(preOrder,DicInOrder, start, pos-1)
        
        #repeat process for right subtree
        root.right = buildTreeRec(preOrder,DicInOrder, pos+1, end)
        
        return root
    return 
        
        
        
    
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
        buildTreeRec.preIndx = 0
        dic_B = {}
        for i in range(len(B)):
            dic_B[B[i]] = i
        return  buildTreeRec(A,dic_B,0,len(B)-1)
        
        
        
