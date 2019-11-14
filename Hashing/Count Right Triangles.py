"""
Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane. Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis. Note: The answer may be large so return the answer modulo (10^9 + 7). 
Input Format
The first argument given is an integer array A.
The second argument given is the integer array B.
Output Format
Return the number of unordered triplets that form a right angled triangle modulo (10^9 + 7).
Constraints
1 <= N <= 100000
0 <= A[i], B[i] <= 10^9 
For Example
Input 1:
    A = [1, 1, 2]
    B = [1, 2, 1]
Output 1:
    1

Input 2:
    A = [1, 1, 2, 3, 3]
    B = [1, 2, 1, 2, 1]
Output 2:
    6
    """
    class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
            
        dic_A = {}
        dic_B = {}
        ans = 0
        for i in range(len(A)):
            if A[i] in dic_A:
                dic_A[A[i]] += 1
            else:
                dic_A[A[i]] = 1

        for i in range(len(B)):
            if B[i] in dic_B:
                dic_B[B[i]] += 1
            else:
                dic_B[B[i]] = 1
                
        for i in range(len(A)):
            X = A[i]
            Y = B[i]
            ans += ((dic_A[X]-1)*(dic_B[Y]-1))
        return ans
                
                
                
                
