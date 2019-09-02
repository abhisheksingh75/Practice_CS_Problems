""" https://www.interviewbit.com/problems/excel-column-title/
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    
"""
class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        returnString = ""
        Dividend =  A
        Divisor = 26
        Quotient, Remainder = 1, 0
        while(Quotient >=1):
            Quotient = Dividend//Divisor
            Remainder = Dividend%Divisor
            #print(Remainder)
            if Remainder == 0:
                Remainder = 26
                Quotient -= 1
            returnString  = chr(64+Remainder) + returnString
            Dividend = Quotient
        return returnString
      
