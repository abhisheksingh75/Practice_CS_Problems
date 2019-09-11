"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        indxBeg, indxEnd = 0, len(A)-1
        canCompare = True
        while(indxBeg<= indxEnd):
            if ((ord(A[indxBeg]) >= 48 and ord(A[indxBeg]) <= 57) or 
                (ord(A[indxBeg]) >= 65 and ord(A[indxBeg]) <= 90) or
                (ord(A[indxBeg]) >= 97 and ord(A[indxBeg]) <= 122)):
                canCompare = True
            else: 
                indxBeg += 1
                canCompare = False
            if canCompare == True:
                if ((ord(A[indxEnd]) >= 48 and ord(A[indxEnd]) <= 57) or 
                    (ord(A[indxEnd]) >= 65 and ord(A[indxEnd]) <= 90) or
                    (ord(A[indxEnd]) >= 97 and ord(A[indxEnd]) <= 122)):
                    canCompare = True
                else: 
                    indxEnd -= 1
                    canCompare = False
                
            if canCompare == True:
                if A[indxBeg].lower() != A[indxEnd].lower():
                    return 0
                else:
                    indxBeg += 1
                    indxEnd -= 1
        return 1    
