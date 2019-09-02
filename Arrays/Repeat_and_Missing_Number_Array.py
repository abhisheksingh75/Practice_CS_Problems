"""https://www.interviewbit.com/problems/repeat-and-missing-number-array/
You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4
"""
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        len_of_A = len(A)
        sumOfN = (len_of_A*(len_of_A+1))>>1
        sumOfN2 = (len_of_A*(len_of_A+1)*(2*len_of_A+1))//6
        sumofAct = 0
        sumofAct2 = 0
        for i in range(len_of_A):
            sumofAct = sumofAct + A[i]
            sumofAct2 += (A[i]*A[i])
                                  
        AminusB = sumOfN-sumofAct
        APlusB  = (sumOfN2-sumofAct2)//AminusB
        
        A = (AminusB+APlusB)>>1
        B = APlusB-A
        return[min(A,B), max(A,B)]
