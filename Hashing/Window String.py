"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity. Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N. Example :
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"
 Note:
If there is no such window in S that covers all characters in T, return the empty string ''.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).
"""
class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def minWindow(self, A, B):
        len_String = len(A)
        len_pattern = len(B)
        #if string length is less than pattern length
        if len_String < len_pattern:
            return ""
        
        # store occurrence ofs characters of pattern  
        dic_pattern = {}
        dic_string ={}
       
        for i in range(len(B)):
            if B[i] in dic_pattern:
                dic_pattern[B[i]] += 1
            else:
                dic_pattern[B[i]] = 1
                
        start, start_indx, min_len = 0, -1, 1<<31
        count = 0
        for j in range(len(A)):
            
            if A[j] in dic_string:
                dic_string[A[j]] += 1
            else:
                dic_string[A[j]] = 1
            
            #increase count of characters 
            if A[j] in dic_pattern and dic_string[A[j]]<=dic_pattern[A[j]]:
                count+= 1
            
            #when count of character in string becomes equal to no of character and frequency sum in     
            if count == len(B):
                
                #keep looping till character is useless or no of start character frequnecy is more than required
                while( A[start] not in dic_pattern or dic_string[A[start]] > dic_pattern[A[start]]):
                    
                    if A[start] in dic_pattern and dic_string[A[start]] > dic_pattern[A[start]]:
                        dic_string[A[start]] -= 1
                    start += 1
                
                len_window = j - start +1
                if min_len > len_window:
                    min_len = len_window
                    start_indx = start
        
        if start_indx == -1:
            return ""
        else:
            return A[start_indx:start_indx+min_len]
               
