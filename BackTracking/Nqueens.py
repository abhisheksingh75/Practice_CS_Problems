"""
NQueens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other. N Queens: Example 1 Given an integer n, return all distinct solutions to the n-queens puzzle. Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively. For example, There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

def formatResult(visited, N):
    format_Sol = [""]*N
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                format_Sol[i] += "."
            else:
                format_Sol[i] += "Q"
    return  format_Sol          



def moveIsPossible(N, curr_row, curr_col, visited):
    
    #no need to check in row as we are doing curr_row+1 for new call
    
    #check in same column
    for i in range(curr_row, -1,-1):
        if visited[i][curr_col] == True:
            return False
    
    #check for left side diagonal
    i = curr_row
    j = curr_col
    while(i >= 0 and j >= 0):
        if visited[i][j] == True:
            return False
        i = i-1
        j = j-1
    
    #check for right side diagonal
    i = curr_row
    j = curr_col
    while(i >= 0 and j <=N-1):
        if visited[i][j] == True:
            return False
        i = i-1
        j = j+1
            
    return True

def backtrackSolveNQueens(N, curr_row, result, visited):
    
    #base case
    if curr_row == N:
        result.append(formatResult(visited, N)) 
    else:
        for i in range(0, N):
            if (moveIsPossible(N, curr_row, i,visited)== True):
                visited[curr_row][i] = True
                backtrackSolveNQueens(N, curr_row+1,result,visited)
                visited[curr_row][i] = False
            

class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        N = A
        result = []
        visited = [[False for i in range(N)] for i in range(N)]
        backtrackSolveNQueens(A,0,result,visited) 
        return result
