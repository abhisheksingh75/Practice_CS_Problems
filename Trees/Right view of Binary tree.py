"""
Given a binary tree of integers. Return an array of integers representing the right view of the Binary tree. Right view of a Binary Tree is a set of nodes visible when the tree is visited from Right side. Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9 
For Example
Input 1:
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Output 1:
    [1, 3, 7, 8]

Input 2:
            1
           /  \
          2    3
           \
            4
             \
              5
Output 2:
    [1, 3, 4, 5]
    
    """
    # Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def rightView(node, currDepth, ans):
    
    if node is None:
        return
    
    if rightView.depth < currDepth:
        ans.append(node.val)
        rightView.depth = currDepth
    
    rightView(node.right, currDepth+1, ans)
    rightView(node.left, currDepth+1, ans)
    
    return 
        
    
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        ans = []
        rightView.depth = -1
        rightView(A, 0, ans)
        return ans
