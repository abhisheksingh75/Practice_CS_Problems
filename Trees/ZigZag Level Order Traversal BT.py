"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between). Example : Given binary tree
    3
   / \
  9  20
    /  \
   15   7
return
[
         [3],
         [20, 9],
         [15, 7]
]
"""
from collections import deque
# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def zigzagLevelOrder2(self, A):
        
        ans = []
        dque = collections.deque()
	    
        if A is None:
            return
        else:
            dque.append(A)
            dque.append(None)
        
        while(len(dque)!= 1):
            curr_level = []
            #pop elements from left till not hitting None
            while(dque[0] is not None):
                node = dque.popleft()
                if node.left is not None:
                    dque.append(node.left)
                if node.right is not None:
                    dque.append(node.right)
                curr_level.append(node.val)
            
            if curr_level != []:   
                ans.append(curr_level)
            curr_level = []
            #pop elements from right till not hitting None
            while(dque[-1] is not None):
                node = dque.pop()
                
                if node.right is not None:
                    dque.appendleft(node.right)
                if node.left is not None:
                    dque.appendleft(node.left)
                curr_level.append(node.val)
                
            if curr_level != []:
                ans.append(curr_level)
            
        return ans
    def zigzagLevelOrder(self, A):
        que = deque()
        revrse = False 
        curr_level = []
        ans = []
        if A is not None:
            que.append(A)
            que.append("$")
        while(que):
            ele = que.popleft()
            if ele == "$":
                if que:
                    que.append("$")
                if revrse:
                    ans.append(curr_level[::-1])
                    revrse = False 
                else:
                    ans.append(curr_level[:])
                    revrse = True 
                curr_level = []
                continue
            
            curr_level.append(ele.val)
            
            if ele.left:
                que.append(ele.left)
            if ele.right:
                que.append(ele.right)
        return ans
            
        
