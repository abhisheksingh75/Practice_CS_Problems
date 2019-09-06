"""
Given an array of integers, every element appears twice except for one. Find that single one. Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? Example :
Input : [1 2 2 3 1]
Output : 3
"""
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def singleNumber(self, A):
	    lenofA = len(A)
	    if len(A) == 1:
	        return A[0]
	    xorAll = A[0]^A[1]
	    for i in range(2, lenofA):
	            xorAll =xorAll^A[i]
	    return xorAll
