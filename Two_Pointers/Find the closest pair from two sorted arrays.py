"""
iven two sorted arrays of distinct integers, A and B, and an integer C, find and return the pair whose sum is closest to C and the pair has one element from each array. More formally, find A[i] and B[j] such that abs((A[i] + B[j]) - C) has minimum value. If there are multiple solutions find the one with minimum i and even if there are multiple values of j for the same i then return the one with minimum j. Note: Return an array with two elements {A[i], B[j]}. 
Input Format
The first argument given is the integer array A.
The second argument given is the integer array B.
The third argument given is integer C.
Output Format
Return the pair which has sum closest to C.
Constraints
1 <= length of both the arrays <= 100000
1 <= A[i], B[i] <= 10^9 
1 <= C <= 10^9
For Example
Input 1:
    A = [1, 2, 3, 4, 5]
    B = [2, 4, 6, 8]
    C = 9
Output 1:
    [1, 8]

Input 2:
    A = [5, 10, 20]
    B = [1, 2, 30]
    C = 13
Output 2:
    [10, 2]
 """
 class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        n = len(A)
        m = len(B)
        min_diff, min_i, min_j = 1<<31, 0,0
        i, j = 0, m-1
        
        while(i<n and j>=0):
            diff = abs(A[i]+B[j]-C)
            #update min_diff, min_i, min_j
            if diff  < min_diff:
                min_diff = diff
                min_i = i
                min_j = j
            elif diff == min_diff:
                if i< min_i:
                    min_i = i
                    min_j = j  
                elif i == min_i:
                    if j < min_j:
                        min_j = j
            #print("min_diff"+str(abs(A[i]+B[j]-C))+"min_i"+str(i)+"min_j"+str(j))
            #decrement j if a[i]+a[j] > C, else increment i
            if A[i]+B[j] >C:
                j -= 1
            else:
                i += 1
        return [A[min_i], B[min_j]]   
            
                    
