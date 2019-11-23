"""
 strstr - locate a substring ( needle ) in a string ( haystack ). 
Try not to use standard library string functions for this question. Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
 NOTE: Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases
"""
def calcLPS(pattern):
    LPS = [0]*len(pattern)
    i, j = 1, 0
    while(i<len(pattern)):
    
        if pattern[i] == pattern[j]:
            LPS[i] = j+1
            i = i+1
            j = j+1
        else:
            if j == 0:
                LPS[i] = 0
                i += 1
            else:
                j = LPS[j-1]
    return LPS



class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	def strStr(self, A, B):
        LPS = []
        LPS = calcLPS(B)
        text = A
        pattern = B
	    
        i,j =0, 0
        while(i<len(text)):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = LPS[j-1]
                else:
                    i += 1
                    
            if j == len(pattern):
                return i-j
	    return -1
	    
	    
