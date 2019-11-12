"""
Given an array of integers A, find the number of sextuplets that satisfy the equation (a * b + c) / d - e = f.
where a, b, c, d, e, f belong to the given array A.
Note: Since the answer can be very large, return the number of ways modulo (109 + 7). 
Input Format
The only argument given is the integer array A.
Output Format
Return the find the number of sextuplets that satisfy the equation.
Constraints
1 <= length of the array <= 100
-10^6 <= A[i] <= 10^6
All elmemts of array A are distinct.
For Example
Input 1:
    A = [1]
Output 1:
    1
    a = b = c = d = e = f = 1 satisfy the equation.

Input 2:
    A = [1, -1]
Output 2:
    24
   """
from collections import defaultdict
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        LHS = {}
        ans = 0\
        len_A = len(A)
        for i in range(len_A):
            for j in range(len_A):
                for k in range(len(A)):
                    lhs_value = ((A[i]*A[j])+A[k])
                    #print("A[i]"+str(A[i])+"A[j]"+str(A[j])+"A[k]"+str(A[k])+"lhs_value"+str(A[i]*A[j]-A[k]))
                    if lhs_value not in LHS:
                        LHS[lhs_value] = 1
                    else:
                        LHS[lhs_value] += 1
        #print(LHS)
        #calc RHS
        for i in range(len(A)):
            if A[i] != 0:
                for j in range(len(A)):
                    for k in range(len(A)):
                        rhs_value = A[i]*(A[j]+A[k])
                        if rhs_value in LHS:
                            #print(rhs_value)
                            ans =(ans+ LHS[rhs_value])%(10**9+7)

        return ans%(10**9+7)                            
                            
                    
                    
