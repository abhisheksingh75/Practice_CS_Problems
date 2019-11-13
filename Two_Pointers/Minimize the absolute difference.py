"""
Given three sorted arrays A, B and Cof not necessarily same sizes. Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that a, b, c belongs arrays A, B, C respectively. i.e. minimize | max(a,b,c) - min(a,b,c) |. Example : Input:
A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:
1
"""
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @param C : list of integers
	# @return an integer
	def solve(self, A, B, C):
        i,j,k = 0,0,0
        min_abs_diff = 1<<31
        
        while(i<len(A) and j<len(B) and k<len(C)):
            
            min_abs_diff = min(min_abs_diff, abs(max(A[i],B[j],C[k])-min(A[i],B[j],C[k])))
            
            if A[i]<=B[j]:
                if A[i]<=C[k]:
                    i += 1
                else:
                    k += 1
            else:
                if B[j]<C[k]:
                    j += 1
                else:
                    k += 1
        return  min_abs_diff
