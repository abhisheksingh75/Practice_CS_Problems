"""
Given the array of strings A, you need to find the longest string S which is the prefix of ALL the strings in the array. Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2. For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc". 
Input Format
The only argument given is an array of strings A.
Output Format
Return longest common prefix of all strings in A.
For Example
Input 1:
    A = ["abcdefgh", "aefghijk", "abcefgh"]
Output 1:
    "a"
    Explanation 1:
        Longest common prefix of all the strings is "a".

Input 2:
    A = ["abab", "ab", "abcd"];
Output 2:
    "ab"
    Explanation 2:
        Longest common prefix of all the strings is "ab".
        """
        class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
        ans = ""
        min_len = min(A, key=len) #calculate minimum len in string  
        
        #if there is only one string
        if len(A) == 1:
            return A[0]
        
        for i in range(len(min_len)):
            for j in range(len(A)-1):
	       
                if A[j][i] == A[j+1][i]:
                    continue
                else:
                    return ans
                    
            ans += A[j][i]
        return ans 
	        
