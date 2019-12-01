"""
Left view of binary tree
"""
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

def leftView(node, currDepth, ans):
    
    if node is None:
        return
    """
    if leftView.depth < currDepth:
        ans.append(node.val)
        leftView.depth = currDepth
    """
    leftView(node.left, currDepth+1, ans)
    if currDepth not in ans:
        ans[currDepth] = node.val
    leftView(node.right, currDepth+1, ans)
    
    return 
        
    
class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        ans = {}
        leftView.depth = -1
        leftView(A, 0, ans)
        result = []
        for key in ans:
            result.append(ans[key])
        return result
