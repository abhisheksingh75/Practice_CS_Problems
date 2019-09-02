"""https://www.interviewbit.com/problems/excel-column-number/
Given a column title as appears in an Excel sheet, return its corresponding column number.

Example:

    A -> 1
    
    B -> 2
    
    C -> 3
    
    ...
    
    Z -> 26
    
    AA -> 27
    
    AB -> 28 
   """
   class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        len_of_string  = len(A)    
        no_of_clmn = 0    
        for i in range(0, len_of_string):
            no_of_clmn = no_of_clmn +((ord(A[i])-64)*(26**(len_of_string-1)))
            len_of_string -= 1
        return no_of_clmn
