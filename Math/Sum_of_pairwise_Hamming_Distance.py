"""https://www.interviewbit.com/problems/sum-of-pairwise-hamming-distance/
Hamming distance between two non-negative integers is defined as the number of positions at which the corresponding bits are different.

For example,

HammingDistance(2, 7) = 2, as only the first and the third bit differs in the binary representation of 2 (010) and 7 (111).

Given an array of N non-negative integers, find the sum of hamming distances of all pairs of integers in the array.
Return the answer modulo 1000000007.

Example

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

import math
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def hammingDistance(self, A):
        binary_no_list = []
        max_len = 0
        sum = 0
        if len(A)  == 1:
            return 0.
        for ele in A:
            binary_no = []
            if ele != 0:
                
                while(ele>0):
                    binary_no.append(str(ele%2))
                    ele = int(math.floor(ele/2)) 
                if len(binary_no) > max_len:
                    max_len = len(binary_no)
            else: 
                binary_no.append('0')
            binary_no_list.append(binary_no) 
        for i in range(0, max_len):
            x, y= 0, 0
            for ele in binary_no_list:
                if len(ele) <= i:
                    x +=1
                elif ele[i] == '0':
                    x +=1
                elif ele[i] == '1':
                    y +=1 
            sum += ((x*y)<<1)
        return sum%1000000007
