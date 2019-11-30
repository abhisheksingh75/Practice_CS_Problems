"""
Binary Tree From Inorder And Postorder
Given inorder and postorder traversal of a tree, construct the binary tree.
 Note: You may assume that duplicates do not exist in the tree. 
Example :
Input : 
        Inorder : [2, 1, 3]
        Postorder : [2, 3, 1]

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

def buildTreeRec(postOrder,DicInOrder, start, end):

    if start == end :
        #create tree node
        root = TreeNode(postOrder[buildTreeRec.preIndx])
        buildTreeRec.preIndx -= 1
        return root
    
    if start < end:
        
        #create tree node
        root = TreeNode(postOrder[buildTreeRec.preIndx])
        buildTreeRec.preIndx -= 1
        
        #find pos of root of sub tree
        pos = DicInOrder[root.val]
        
        #repeat process for right subtree
        root.right = buildTreeRec(postOrder,DicInOrder, pos+1, end)
        
        #repeat process for left subtree
        root.left = buildTreeRec(postOrder,DicInOrder, start, pos-1)
        return root
    return 
        
        
        
    
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return the root node in the tree
	def buildTree(self, A, B):
	    A,B = B,A
        buildTreeRec.preIndx = len(B)-1
        dic_B = {}
        for i in range(len(B)):
            dic_B[B[i]] = i
        return  buildTreeRec(A,dic_B,0,len(B)-1)
        
        
        
          
