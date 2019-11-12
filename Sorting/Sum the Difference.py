"""
Given an Array of numbers You have to find all possible non-empty subsets of the array of numbers and then, for each subset, find the difference between the largest and smallest numbers in that subset Then add up all the differences to get the number. As the number may be large, output the number modulo 1e9 + 7 (1000000007).
Example:

A = [1, 2]

All subsets
[1]    largest-smallest = 1 - 1 = 0
[2]    largest-smallest = 2 - 2 = 0
[1 2]  largest-smallest = 2 - 1 = 1

Sum of the differences = 0 + 0 + 1 = 1

So resultant number is 1
Constraints:
1 ≤ N ≤ 10000
"""

#sort the array
#if size is N. each element will be part of 2**(N-1)
#if Array = [a0,a1,a2...ai....an], each element will be smallest in subseq-[a0-2**(N-1),a1-2**(N-2)...Ai-2**(N-i)...A(n-1)-2**0]
#if Array = [a0,a1,a2...ai....an], each element will be largest in subseq-[a0-2**0,a1-2**1...Ai-2**(i-1)...A(n-1)-2**(N-1)]

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
	    A.sort()
	    N = len(A)
	    sumOfsmallest,sumOfLargest = 0, 0
	    for i in range(len(A)):
	        sumOfsmallest += (A[i]*(2**(N-i-1)))
	        
	    for i in range(len(A)):
	        sumOfLargest += (A[i]*(2**i))	 
	        
	    diff =  (sumOfLargest-sumOfsmallest)
	    return diff%1000000007
	        
	        
	        
	    
    
