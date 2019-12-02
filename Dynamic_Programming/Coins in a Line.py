"""
There are A coins (Assume A is even) in a line. Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins. Assume that you go first. Return the maximum amount of money you can win. Input Format:
The first and the only argument of input contains an integer array, A.
Output Format:
Return an integer representing the maximum amount of money you can win.
Constraints:
1 <= length(A) <= 500
1 <= A[i] <= 1e5
Examples:
Input 1:
    A = [1, 2, 3, 4]

Output 1:
    6

Explanation 1:

    You      : Pick 4
    Opponent : Pick 3
    You      : Pick 2
    Opponent : Pick 1

    Total money with you : 4 + 2 = 6

Input 2:
    A = [5, 4, 8, 10]

Output 2:
    15

Explanation 2:

    You      : Pick 10
    Opponent : Pick 8
    You      : Pick 5
    Opponent : Pick 4

    Total money with you : 10 + 5 = 15
    """
    
                """
def RecMax(A, start, end,dicSubProb):

    if end == start:
        return A[start]
    if end-start <= 1:
        dicSubProb[(start, end)] = max(A[end], A[start])
        return dicSubProb[(start, end)] 
    if (start, end) in dicSubProb:
        return dicSubProb[(start, end)]
    
    #ele = A[start]
    sum = max(min(RecMax(A, start+2, end,dicSubProb),RecMax(A, start+1, end-1,dicSubProb)),min(RecMax(A, start+1, end-1,dicSubProb),RecMax(A, start, end-2,dicSubProb)))
    dicSubProb[(start, end)] = sum
    
    return dicSubProb[(start, end)]
    
    
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxcoin(self, A):
        dicSubProb = {}
        return RecMax(A,0,len(A)-1,dicSubProb)
"""  

def recMaxCoins(player, start, end, A, DP):
    if start > end:
        return 0
    if DP[player][start][end] != -1:
        return DP[player][start][end]
    if player == 0:
        DP[player][start][end] = max(recMaxCoins(1, start+1, end, A, DP)+A[start],recMaxCoins(1, start, end-1, A, DP)+A[end])
        return DP[player][start][end]
    else:
        DP[player][start][end] = min(recMaxCoins(0, start+1, end, A, DP),recMaxCoins(0, start, end-1, A, DP))
        return DP[player][start][end]
        
class Solution:
	# @param A : list of integers
	# @return an integer
	def maxcoin(self, A):
	    DP = [[[ -1 for i in range(len(A))] for j in range(len(A))] for k in range(2)]
	    return recMaxCoins(0, 0, len(A)-1, A, DP)
	    
	    
        

