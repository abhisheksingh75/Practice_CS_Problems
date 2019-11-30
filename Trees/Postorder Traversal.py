"""
Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values. Example : Given binary tree
   1
    \
     2
    /
   3
return [3,2,1]. Using recursion is not allowed.
"""


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):

        ans = []
        stack = []
        
        #check for base case
        if A is None:
            return 
        else:
            stack.append(A)
        
        while(stack != []):
            ele = stack.pop()
            #check if left element exist push it
            if ele.left is not None:
                stack.append(ele.left)
            #check if right elemtne exist push it
            if ele.right is not None:
                stack.append(ele.right)
            
            ans.append(ele.val)
                    
        return ans[::-1]
        
        
        
        
            
        
