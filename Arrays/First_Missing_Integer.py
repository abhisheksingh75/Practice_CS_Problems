"""https://www.interviewbit.com/courses/programming/topics/arrays/
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        missingNumber = 0
        N = len(A)
        i = 0
        tmp = A[i]
        while(i<N):
            if A[i]<= 0  or A[i] > N:
                A[i] = -1
                i += 1
            elif A[i] == i or A[i] == A[A[i]-1]:
                i += 1
            else:
                tmp = A[A[i]-1] 
                A[A[i]-1] = A[i]
                A[i] = tmp 
            #print(A)    
        for i in range(N): 
            if A[i] < 0:
               break
            missingNumber = A[i]
        return missingNumber+1
