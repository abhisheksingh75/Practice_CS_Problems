"""
Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

Examples :
Input
0 2 5 7
Output
2 (0 XOR 2)
Input
0 4 7 9
Output
3 (4 XOR 7)

Constraints:
2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000
"""
class Solution:
	# @param A : list of integers
	# @return an integer
	def findMinXor(self, A):
	    A.sort()
	    min_XOR = 1<<32
	    for i in range(len(A)-1):
	         min_XOR = min(A[i]^A[i+1],  min_XOR)
	    return min_XOR
	        
