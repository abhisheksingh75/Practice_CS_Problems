"""
Given a binary tree of integers. Return an array of integers representing the Top view of the Binary tree. Top view of a Binary Tree is a set of nodes visible when the tree is visited from Top side. Note: Return the nodes in any order. Constraints
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
    [1, 2, 4, 8, 3, 7]

Input 2:
            1
           /  \
          2    3
           \
            4
             \
              5
Output 2:
    [1, 2, 3]
    """
    # Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def topView(node, Horizon, dicAns):
    
    if node is None:
        return
    if Horizon not in dicAns:
        dicAns[Horizon] = node.val
        
    topView(node.left,Horizon-1,dicAns)
    topView(node.right,Horizon+1,dicAns)
    return 

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        dic_ans = {}
        ans = []
        topView(A, 0, dic_ans)
        for key in sorted(dic_ans):
            ans.append(dic_ans[key])
        return ans
    
