"""
Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx The Sudoku board could be partially filled, where empty cells are filled with the character '.'.  The input corresponding to the above configuration :
["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
A partially filled sudoku which is valid.
 Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
class Solution:
	# @param A : tuple of strings
	# @return an integer
	def isValidSudoku(self, A):
        
        #check rowwise  sudoko is valid or not 
        for i in range(9):
            dic_ele = {}
            for j in range(9):
                if A[i][j] != '.' and A[i][j] not in dic_ele:
                    dic_ele[A[i][j]] = 1
                elif A[i][j] in dic_ele:
                    #print("rowwise")
                    return 0
            
        #check colwise  sudoko is valid or not 
        for i in range(9):
            dic_ele = {}
            for j in range(9):
                if A[j][i] != '.' and A[j][i] not in dic_ele:
                    dic_ele[A[j][i]] = 1
                elif A[j][i] in dic_ele:
                    #print("colwise"+"i:"+str(i)+"j:"+str(j))
                    return 0
        
        #check for each 3*3 block
        N = 1
        while(N<=9):
            #determine col block wise
            if N%3 == 1:
                start_j, end_j = 0, 3
            elif N%3 == 2:
                start_j, end_j = 3, 6
            elif N%3 == 0:
                start_j, end_j = 6, 9
            #determine row block wise
            if (N-1)//3 == 0:
                start_i, end_i = 0, 3
            elif (N-1)//3 == 1:
                start_i, end_i = 3, 6
            elif (N-1)//3 == 2:
                start_i, end_i = 6, 9
            dic_ele = {}
            
            for i in range(start_i, end_i, 1):
                for j in range(start_j,end_j,1):
                    if A[i][j] != '.' and A[i][j] not in dic_ele:
                        dic_ele[A[i][j]] = 1
                    elif A[i][j] in dic_ele:
                        #print("block")
                        return 0
            #print("N"+str(N)+str(dic_ele))
            N += 1
        return 1
        
        
