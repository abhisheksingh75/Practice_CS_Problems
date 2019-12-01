"""
Given a binary tree. Check whether the given tree is a Sum-binary tree or not. SumTree is a Binary Tree where the value of a node is equal to sum of the nodes present in its left subtree and right subtree. An empty tree is SumTree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree. Return 1 if it sum-binary tree else return 0. 
Input Format
The only argument given is the root pointer of tree A.
Output Format
Return 1 if it is sum-binary tree else return 0.
Constraints
1 <= length of the array <= 100000
0 <= node values <= 50
For Example
Input 1:
       26
     /    \
    10     3
   /  \     \
  4   6      3
Output 1:
    1

Input 2:
       26
     /    \
    10     3
   /  \     \
  4   6      4
Output 2:
    0
    """
    
        
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def isSumBinaryTree(node):
    
    if node is None:
        return [True, 0]
    else:
        isLeftBT = isSumBinaryTree(node.left)
        isRightBT = isSumBinaryTree(node.right)
        sum = isLeftBT[1] + isRightBT[1] + node.val
    if node.left is not None and node.right is not None:
        if isLeftBT[0] == True and isRightBT[0] == True and (isLeftBT[1] + isRightBT[1] == node.val):
            return [True, sum]
        else:
            return [False, sum]
            
    elif node.left is not None:
        if isLeftBT[0] == True and isLeftBT[1]  == node.val:
            return [True, sum]
        else:
            return [False, sum]
    elif node.left is not None:
        if isRightBT[0] == True and isRightBT[1] == node.val:
            return [True, sum]
        else:
            return [False, sum]
    else:
        #if node.left is None and node.right is None:
        return [True, sum]

def isSumBinaryTree2(node):
    
    if node is None:
        return 0 
    elif node.left is None and node.right is None:
        return node.val 
    else:
        left_val = isSumBinaryTree2(node.left)
        right_val = isSumBinaryTree2(node.right)
        if left_val >=0 and right_val>= 0:
            if node.val == left_val+right_val:
                return left_val+right_val+node.val
            else:
                return -1
        else:
            return -1
        
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        return 1 if isSumBinaryTree2(A) >= 0 else 0
