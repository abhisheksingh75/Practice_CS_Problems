"""
um of pairwise Hamming Distance
Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different. For example, HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111). Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array. Return the answer modulo 1000000007. Example
Let f(x, y) be the hamming distance defined above.

A=[2, 4, 6]

We return,
f(2, 2) + f(2, 4) + f(2, 6) + 
f(4, 2) + f(4, 4) + f(4, 6) +
f(6, 2) + f(6, 4) + f(6, 6) = 

0 + 2 + 1
2 + 0 + 1
1 + 1 + 0 = 8
"""
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def hammingDistance(self, A):
        hamming_distance = 0
        count_of_bits = [0]*32
        
        if len(A) == 1:
            return 0
            
        for i in range(len(A)):
            for k in range(32):
                if(A[i]&(1<<k)):
                    count_of_bits[k] += 1
        for i in range(32):
            hamming_distance += (count_of_bits[i]*(len(A)-count_of_bits[i])) 
        return (hamming_distance*2)%1000000007
