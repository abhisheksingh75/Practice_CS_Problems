"""https://www.interviewbit.com/problems/palindrome-integer/

Determine whether an integer is a palindrome. Do this without extra space.

A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
Negative numbers are not palindromic.

Example :

Input : 12121
Output : True

Input : 123
Output : False
"""
class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        
        if A < 0:
            return 0
        len_of_A = len(str(A))
        i, beg, end, num1, num2 = 0,0,0,A,A
        while(i < len_of_A//2):
            beg =  num1//(10**(len_of_A-1-i))
            end =  num2%(10**(i+1))
            num1 = num1//(10**(len_of_A-1-i))
            num2 = num2//(10**(i+1))
            print(beg)
            print(end)
            if beg != end:
                return 0
        return 1
