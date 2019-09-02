"""https://www.interviewbit.com/problems/trailing-zeros-in-factorial/
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120 
Number of trailing zeros = 1
So, return 1Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120 
Number of trailing zeros = 1
So, return 1
"""
import math
class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        no_of_tzeros = 0
        i = 1
        while(5**i <= A):
            no_of_tzeros += int(math.floor(A/(5**i)))
            i += 1
        
        return no_of_tzeros
