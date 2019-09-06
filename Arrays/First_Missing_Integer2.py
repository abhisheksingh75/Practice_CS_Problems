"""
Given an unsorted integer array, find the first missing positive integer. 
Example: Given [1,2,0] return 3, [3,4,-1,1] return 2, [-8, -7, -6] returns 1 
Your algorithm should run in O(n) time and use constant space.
"""

class Solution:
    def firstMissingPositive(self, A):
        N = len(A)
        i = 0
        tmp = 0
        while(i < N):
            
            if A[i] < 1 or A[i] > N or A[i] == i+1 or A[A[i]-1] == A[i]:
                i += 1
                continue
            else:
                tmp = A[A[i]-1] 
                A[A[i]-1] = A[i]
                A[i] = tmp 
            
        for i in range(len(A)):
            if A[i] != i+1:
                return i+1
        
        return N+1
                
