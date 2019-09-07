"""
Given a 2D Matrix of dimensions N*N, we need to return sum of all possible submatrices. Example Input
[ [1,1],
  [1,1] ]
Example Output
16
Explanation
Number of submatrices with 1 elements = 4, so sum of all such submatrices = 4*1 = 4
Number of submatrices with 2 elements = 4, so sum of all such submatrices = 4*2 = 8
Number of submatrices with 3 elements = 0
Number of submatrices with 4 elements = 1, so sum of such submatrix = 4

Total Sum = 4+8+4 = 16
"""
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        all_sum  = 0
        N = len(A)
        for i in range(N):
            for j in range(N):
                #print ("above"+str((i+1)*(j+1)))
                #print ("below"+str((N-i)*(N-i)))
                all_sum = all_sum + (A[i][j]*(i+1)*(j+1)*(N-i)*(N-j))
                #print (all_sum)
            
        return all_sum
        
       
