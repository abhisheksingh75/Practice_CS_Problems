"""
Given an string A. The only operation allowed is to insert characters in the beginning of the string. Find how many minimum characters are needed to be inserted to make the string a palindrome string. 
Input Format
The only argument given is string A.
Output Format
Return the minimum characters that are needed to be inserted to make the string a palindrome string.
For Example
Input 1:
    A = "ABC"
Output 1:
    2
    Explanation 1:
        Insert 'B' at beginning, string becomes: "BABC".
        Insert 'C' at beginning, string becomes: "CBABC".

Input 2:
    A = "AACECAAAA"
Output 2:
    2
    Explanation 2:
        Insert 'A' at beginning, string becomes: "AAACECAAAA".
        Insert 'A' at beginning, string becomes: "AAAACECAAAA".
       """
       def calcLPS(pattern):
    LPS = [0]*len(pattern)
    i = 1
    j = 0
    while(i<len(pattern)):
        if pattern[i] == pattern[j]:
            LPS[i] = j+1
            i += 1
            j += 1
            
        else:
            #pattern[i] != pattern[j]
            if j == 0:
                LPS[i] = 0
                i += 1
            else:
                j = LPS[j-1]
    return LPS

class Solution:
	# @param A : string
	# @return an integer
	def solve(self, A): 
	    LPS = []
	    string = A+"$"+A[::-1]
	    LPS =  calcLPS(string)
	    
	    return len(A)-LPS[len(LPS)-1]
        
