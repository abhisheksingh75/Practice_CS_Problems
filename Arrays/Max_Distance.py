"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j]. If there is no solution possible, return -1. Example :
A : [3 5 4 2]

Output : 2 
for the pair (3, 4)
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        AUX_A = [[0 for i in range(2)]for j in range(len(A))]
        max_j = [-1]*(len(A)+1)
        max_j_minus_i = -1
        if len(A) == 1:
            return 0
        
        for i in range(len(A)):
            AUX_A[i][0] = A[i]
            AUX_A[i][1] = i
        AUX_A.sort(key = lambda x:x[0])
        
        #print(AUX_A)
        #pre-compute the max_j for given i
        for i in range(len(A)-1,-1, -1):
            max_j[i] =  max(AUX_A[i][1], max_j[i+1])
        
        #print(max_j)
        for i in range(len(A)-1):
            max_j_minus_i = max(max_j_minus_i,  max_j[i]- AUX_A[i][1])
            #print(max_j_minus_i)
        
        return max_j_minus_i
            
            
            
