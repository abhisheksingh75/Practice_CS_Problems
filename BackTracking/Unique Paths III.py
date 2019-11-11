"""
iven a matrix of integers A of size N x M. There are 4 types of squares in it:
1. 1 represents the starting square.  There is exactly one starting square.
2. 2 represents the ending square.  There is exactly one ending square.
3. 0 represents empty squares we can walk over.
4. -1 represents obstacles that we cannot walk over.
Find and return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once. Note: Rows are numbered from top to bottom and columns are numbered from left to right. 
Input Format
The first argument given is the integer matrix A.
Output Format
Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly once.
Constraints
2 <= N * M <= 20
-1 <= A[i] <= 2
For Example
Input 1:
    A = [   [1, 0, 0, 0]
            [0, 0, 0, 0]
            [0, 0, 2, -1]   ]
Output 1:
    2
Explanation 1: We have the following two paths: 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Input 2:
    A = [   [0, 1]
            [2, 0]    ]
Output 2:
    0
    """
    def allVisitedPath(A,matrix):
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            if (((A[i][j] == 1 or A[i][j] == 2 or A[i][j] == 0) and matrix[i][j] == True) or
                (A[i][j] == -1 and matrix[i][j] == False)):
                continue
            else:
                return False
    return True
     
def moveIsValid(A,visited,i,j):
    

    if (i < len(A) and j < len(A[0]) and
    i >= 0 and j>=0 and 
    A[i][j] != -1 and visited[i][j] == False):
        return True
    else:
        return False
        

def backtrackingSolve(result, A, i,j, visited,n,m):
    
    if (i == n and j == m) and allVisitedPath(A,visited) == True:
        result[0] += 1
    else:
        #check for up move
        if moveIsValid(A, visited, i-1, j) == True:
            visited[i-1][j] = True
            backtrackingSolve(result, A, i-1, j, visited,n,m)
            visited[i-1][j] = False
        
        #check for right move
        if moveIsValid(A, visited, i, j+1) == True:
            visited[i][j+1] = True
            backtrackingSolve(result, A, i, j+1, visited,n,m)
            visited[i][j+1] = False

        #check for down move
        if moveIsValid(A, visited, i+1, j) == True:
            visited[i+1][j] = True
            backtrackingSolve(result, A, i+1, j, visited,n,m)
            visited[i+1][j] = False
            
        #check for left move
        if moveIsValid(A, visited, i, j-1) == True:
            visited[i][j-1] = True
            backtrackingSolve(result, A, i, j-1, visited,n,m)
            visited[i][j-1] = False
            
    return    


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        result = [0]*1
        visited = [[False for j in range(len(A[0]))] for i in range(len(A))]
        visited[0][0] = True
        start_i, start_j, end_i, end_j = 0,0,0,0
        
        #calc start_i and start_j
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    start_i = i
                    end_j = j
                    break
                
        #calc end_i and end_j
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 2:
                    end_i = i
                    end_j = j
                    break
        
        backtrackingSolve(result, A, start_i,start_j, visited,end_i,end_j)
        return result[0]
