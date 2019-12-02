"""
Given an array of integers, A of length N, find the length of longest subsequence which is first increasing then decreasing. Input Format:
The first and the only argument contains an integer array, A.
Output Format:
Return an integer representing the answer as described in the problem statement.
Constraints:
1 <= N <= 3000
1 <= A[i] <= 1e7
Example:
Input 1:
    A = [1, 2, 1]

Output 1:
    3

Explanation 1:
    [1, 2, 1] is the longest subsequence.

Input 2:
    [1, 11, 2, 10, 4, 5, 2, 1]

Output 2:
    6

Explanation 2:
    [1 2 10 4 2 1] is the longest subsequence.
    """
    class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestSubsequenceLength(self, A):
	    
	    if len(A) <= 0:
	        return 0
	    
        maxLen = 1
        leftLIS = [1]*len(A)
        rightLIS = [1]*len(A)
         
        #populate LIS from left to right
        for i in range(1, len(A)):
             for j in range(i):
                 if A[i] > A[j]:
                     leftLIS[i] = max(leftLIS[i],leftLIS[j]+1)
                     
        #populate LIS from right to left
        for i in range(len(A)-2, -1, -1):
            
            for j in range(len(A)-1, i, -1):
                
                if A[i] > A[j]:
                   rightLIS[i] = max(rightLIS[i], rightLIS[j]+1)
                   
                   
        #find max length of longest subsequence which is first increasing then decreasing.
        for i in range(len(A)):
            maxLen = max(maxLen, (leftLIS[i]+rightLIS[i]-1))
        return maxLen
	 
	   
	       
