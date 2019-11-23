"""
Given two strings A and B. Check if B contains same characters as that of given string A and in the same order. Note
 1: A and B contain only UPPERCASE Letters.
2: No two consecutive characters are same in A.
3: You can only use constant amount of extra memory.
"""
The first argument given is string A.
The second argument given is string B.
Output Format
Return 1 if B contains same characters as that of given string A and in the same order else return 0.
For Example
Input 1:
    A = "HIRED" 
    B = "HHHIIIRRRRREEEEEDDDDD"
Output 1:
    1

Input 2:
    A = "HIRED"
    B = "DDHHHHIIIIRRRRREEEEDDD"
Output 2:
    0
   """
   class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        
        i, j =0,0
        while(i<len(A) and j<len(B)):
            if i< len(A) and j <len(B) and A[i] != B[j]:
                return 0
            while(j<len(B) and A[i] == B[j]):
                j += 1
            i += 1
            
                
        if i == len(A) and j == len(B):
            return 1
        else:
            return 0
            
