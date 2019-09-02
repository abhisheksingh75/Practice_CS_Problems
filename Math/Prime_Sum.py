"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture

Example:


Input : 4
Output: 2 + 2 = 4

https://www.interviewbit.com/problems/prime-sum/
"""

from math  import ceil, sqrt
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        return_numbers = []
        prime_numbers = {}
        prime_numbers = self.sieveOfErantosthense(A)        
        
        for key in sorted(prime_numbers):
            if A-key in prime_numbers:
               return_numbers.append(key)
               return_numbers.append(A-key)
               return return_numbers
            
    def sieveOfErantosthense(self, A):
        prime_numbers = {}
        prime_list = [True]*A
        prime_list[0] = False
        prime_list[1] = False   
        for i in range(2, ceil(sqrt(A))):
            if prime_list[i] == True:
                for j in range(2*i, A, i):
                    prime_list[j] = False
        for i in range(A):
            if prime_list[i] == True:
                prime_numbers[i] = True
        return prime_numberss
        
