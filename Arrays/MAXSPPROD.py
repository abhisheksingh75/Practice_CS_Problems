"""https://www.interviewbit.com/problems/maxspprod/
You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:<ul>

LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). If multiple A[j]’s are present in multiple positions, the LeftSpecialValue is the maximum value of j. 

RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If multiple A[j]s are present in multiple positions, the RightSpecialValue is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.

Input: You will receive array of integers as argument to function.

Return: Maximum special product of any integer in the array modulo 1000000007.

Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.

Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        lsv_stack = []
        lsv_final = []
        lsv_indx  = []
        
        rsv_stack = []
        rsv_final = []
        rsv_indx  = []
        
        max_special_pro = -1*(1<<31)
        for i in range(len(A)):          
            while lsv_stack != [] and lsv_stack[-1] <= A[i]:
                lsv_stack.pop()
                lsv_indx.pop()
        
            if lsv_stack == []:
                lsv_final.append(0)   
            else:
                lsv_final.append(lsv_indx[-1])                  
            lsv_stack.append(A[i]) 
            lsv_indx.append(i)
            
        for i in range(len(A)-1, -1, -1):
            while rsv_stack != [] and rsv_stack[-1] <= A[i]:
                  rsv_stack.pop()
                  rsv_indx.pop()
            
            if rsv_stack == []:
               rsv_final.append(0)
            else:
                rsv_final.append(rsv_indx[-1])
            rsv_stack.append(A[i])
            rsv_indx.append(i)             
        rsv_final = rsv_final[::-1]
        
        for i in range(len(A)):
            max_special_pro = max(max_special_pro, lsv_final[i]*rsv_final[i])
        return max_special_pro%1000000007  
