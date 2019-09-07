"""
Given a matrix of integers A of size N x M and an integer B. In the given matrix every row and column is sorted in increasing order. Find and return the position of B in the matrix in the given form:
If A[i][j] = B then return (i * 1009 + j)
And if B is not present return -1 instead. Note: Rows are numbered from top to bottom and columns are numbered from left to right. 
Input Format
The first argument given is the integer matrix A.
The second argument given is the integer B.
Output Format
Return the position of B and if it is not present in A return -1 instead.
Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
-100000 <= B <= 100000
For Example
Input 1:
    A = [   [1, 2, 3]
            [4, 5, 6]
            [7, 8, 9]   ]
    B = 2
Output 1:
    1011    (= 1 * 1009 + 2)

Input 2:
    A = [   [1, 3, 5, 7]
            [2, 4, 6, 8]    ]
    B = 10
Output 2:
    -1
    """
    class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i, j = 0, len(A[0])-1
        rows,cols = len(A), len(A[0])
        while(i <rows and j >= 0):
            
            if A[i][j] == B:
                i = i+ 1
                j = j+1
                return (i*1009)+j
            elif B > A[i][j] :
                i = i+1
            elif B < A[i][j]:
                j = j-1
        return -1       
