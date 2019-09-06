"""
Find the contiguous subarray within an array, A of length N which has the largest sum. Input Format:
The first and the only argument contains an integer array, A.
Output Format:
Return an integer representing the maximum possible sum of the contiguous subarray.
Constraints:
1 <= N <= 1e6
-1000 <= A[i] <= 1000
For example:
Input 1:
    A = [1, 2, 3, 4, -10]

Output 1:
    10

Explanation 1:
    The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

Input 2:
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output 2:
    6
    """
    class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        global_max, local_max = A[0], A[0]
        for i in range(1, len(A), 1):
            local_max = max(local_max+A[i], A[i])
            global_max = max(local_max,global_max)
        return global_max
