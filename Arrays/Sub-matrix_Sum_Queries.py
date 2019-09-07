"""
Given a matrix of integers A of size N x M and multiple queries Q, for each query find and return the submatrix sum. Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out. Note: Rows are numbered from top to bottom and columns are numbered from left to right. Sum may be large so return the answer mod 10^9 + 7. 
Input Format
The first argument given is the integer matrix A.
The second argument given is the integer array B.
The third argument given is the integer array C.
The fourth argument given is the integer array D.
The fifth argument given is the integer array E.
(B[i], C[i]) represents the top left corner of the i'th query.
(D[i], E[i]) represents the bottom right corner of the i'th query.
Output Format
Return the submatrix sum (% 10^9 + 7) for each query in the form of an integer array.
Constraints
1 <= N, M <= 1000
-100000 <= A[i] <= 100000
1 <= Q <= 100000
1 <= B[i] <= D[i] <= N
1 <= C[i] <= E[i] <= M
For Example
Input 1:
    A = [   [1, 2, 3]
            [4, 5, 6]
            [7, 8, 9]   ]
    B = [1, 2]
    C = [1, 2]
    D = [2, 3]
    E = [2, 3]
Output 1:
    [12, 28]

Input 2:
    A = [   [5, 17, 100, 11]
            [0, 0,  2,   8]    ]
    B = [1, 1]
    C = [1, 4]
    D = [2, 2]
    E = [2, 4]
Output 2:
    [22, 19]
    """
    
    class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A,B,C,D,E):
        rows = len(A)
        cols = len(A[0])
        lenOfB = len(B)
        a,b,c,d = 0, 0 ,0 ,0
        return_list = [0]*lenOfB
        for i in range(rows):
            for j in range(1, cols, 1):
                A[i][j] = A[i][j] + A[i][j-1]
        
        for i in range(rows):
            for j in range(cols):
                if i-1 >= 0:
                    A[i][j] = A[i][j] + A[i-1][j]
        
        #print(A)        
        for i in range(lenOfB):
            a,b = B[i]-1,C[i]-1
            c,d = D[i]-1,E[i]-1
            return_list[i] = A[c][d]
            if a > 0:
                return_list[i] = return_list[i] - A[a-1][d] 
            if b > 0:
                return_list[i] = return_list[i] - A[c][b-1]
            if a > 0 and b > 0:
                return_list[i] = return_list[i] + A[a-1][b-1]  
            return_list[i] = return_list[i]%(1000000000 + 7)
                
        return  return_list  
        
