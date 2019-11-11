"""
Given an array of integers A, the array is squareful if for every pair of adjacent elements, their sum is a perfect square. Find and return the number of permutations of A that are squareful. Two permutations A1 and A2 differ if and only if there is some index i such that A1[ i ] != A2[ i ]. 
Input Format
The only argument given is the integer array A.
Output Format
Return the number of permutations of A that are squareful.
Constraints
1 <= length of the array <= 12
1 <= A[i] <= 10^9 
For Example
Input 1:
    A = [2, 2, 2]
Output 1:
    1

Input 2:
    A = [1, 17, 8]
Output 2:
    2
    """
    def Squarefulness(A,B):
    sum = A+B
    root = int(math.floor(math.sqrt(sum)))
    if root*root == sum:
        return True
    else:
        return False
    
def backtrackPremuteSolve(A,result, curr_row, N):
    
    if curr_row > 1 and Squarefulness(A[curr_row-1],A[curr_row-2]) == False:
        return
    if curr_row == N-1 and Squarefulness(A[curr_row],A[curr_row-1]) == False:
        return
    if curr_row == N-1:
        #print(A)
        result[0] += 1
    else:
        dic_visited = {}
        for i in range(curr_row, N):
            if  A[i] not in dic_visited:
                dic_visited[A[i]] = 1
                A[curr_row],  A[i] = A[i], A[curr_row]
                backtrackPremuteSolve(A, result, curr_row+1, N)
                A[curr_row],  A[i] = A[i], A[curr_row]



class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        result = [0]*1
        temp = []
        backtrackPremuteSolve(A, result,0, len(A))
        return result[0]
class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        ans = []
        N = 2**A
        for i in range(N):
            ans.append(i^(i>>1))
        return ansdef Squarefulness(A,B):
    sum = A+B
    root = int(math.floor(math.sqrt(sum)))
    if root*root == sum:
        return True
    else:
        return False
    
def backtrackPremuteSolve(A,result, curr_row, N):
    
    if curr_row > 1 and Squarefulness(A[curr_row-1],A[curr_row-2]) == False:
        return
    if curr_row == N-1 and Squarefulness(A[curr_row],A[curr_row-1]) == False:
        return
    if curr_row == N-1:
        #print(A)
        result[0] += 1
    else:
        dic_visited = {}
        for i in range(curr_row, N):
            if  A[i] not in dic_visited:
                dic_visited[A[i]] = 1
                A[curr_row],  A[i] = A[i], A[curr_row]
                backtrackPremuteSolve(A, result, curr_row+1, N)
                A[curr_row],  A[i] = A[i], A[curr_row]



class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        result = [0]*1
        temp = []
        backtrackPremuteSolve(A, result,0, len(A))
        return result[0]
