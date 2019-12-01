"""
ertical Order traversal of Binary Tree
Given a binary tree, return a 2-D array with vertical order traversal of it. Go through the example and image for more details. Example : Given binary tree:
      6
    /   \
   3     7
  / \     \
 2   5     9
returns
[
    [2],
    [3],
    [6 5],
    [7],
    [9]
]
"""
# Definition for a  binary tree node
from collections import defaultdict 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def verticalOrderTraversalRec(node, curr_level, ans, height):
    
    if node is None:
        return
    ans[curr_level].append([node.val, height])
    verticalOrderTraversalRec(node.left, curr_level-1, ans, height+1)
    verticalOrderTraversalRec(node.right, curr_level+1, ans,height+1)
    
    
    

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        dic_ans = defaultdict(list)
        ans = []
        verticalOrderTraversalRec(A, 0, dic_ans, 0)
        for key in sorted(dic_ans):
            curr_list = dic_ans[key]
            tmp = []
            #print(curr_list)
            curr_list.sort(key = lambda x:x[1])
            ans.append([x[0] for x in curr_list])
        return ans
