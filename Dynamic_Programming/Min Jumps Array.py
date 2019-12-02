"""
Given an array of non-negative integers, A, of length N, you are initially positioned at the first index of the array. Each element in the array represents your maximum jump length at that position. Return the minimum number of jumps required to reach the last index. If it is not possible to reach the last index, return -1. Input Format:
The first and the only argument contains an integer array, A.
Output Format:
Return an integer, representing the answer as described in the problem statement.
Constraints:
1 <= N <= 1e6
0 <= A[i] <= 50000
Examples:
Input 1:
    A = [2, 1, 1]

Output 1:
    1

Explanation 1:
    The shortest way to reach index 2 is
        Index 0 -> Index 2
    that requires only 1 jump.

Input 2:
    A = [2,3,1,1,4]

Output 2:
    2

Explanation 2:
    The shortest way to reach index 4 is
        Index 0 -> Index 1 -> Index 4
    that requires 2 jumps.
    """
    class Solution:
	# @param A : list of integers
	# @return an integer
	def jump(self, A):
            
        if len(A) == 1:
            return 0
        elif len(A) > 1:
            if A[0] == 0:
                return -1
        jumps = 1
        maxreach = A[0]
        steps = A[0]
        for i in range(1, len(A)):
            
            if i == len(A)-1:
                return jumps
            
            maxreach = max(maxreach, A[i] + i)
            
            steps -= 1
            
            if steps == 0:
                jumps += 1
                if i >= maxreach:
                    return -1
                else:
                    steps = maxreach - i
        return jumps
