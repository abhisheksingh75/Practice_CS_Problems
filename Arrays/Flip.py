"""https://www.interviewbit.com/problems/flip/
You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

Notes:

Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.
For example,

S = 010

Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].
Another example,

If S = 111

No operation can give us more than three 1s in final string. So, we return empty array [].
"""
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        A = [int(item) for item in A]
        currmax = 0
        max = 0
        curr_i, currj = None, None
        max_i, max_i = None, None
        for i in range(len(A)):
            if  A[i] == 1:
                A[i] = -1
            else:
                A[i] = 1
        
        for i in range(len(A)):          
            if currmax + A[i] >= A[i]:
                currmax = currmax + A[i]
                curr_j = i
                if curr_i is None:
                    curr_i  = i
            else:
                currmax = A[i]
                curr_i = i
                curr_j  = i
            if max < currmax:
                max = currmax
                max_i = curr_i
                max_j = curr_j
            elif max == currmax:
                if max_i > curr_i:
                    max_i = curr_i  
                    max_j = curr_j   
                elif max_i == curr_i:
                    if max_j > curr_j:
                        max_i = curr_i  
                        max_j = curr_j  
                      
        if max_i is None :
            return []
        else:
            return [max_i+1, max_j+1]
