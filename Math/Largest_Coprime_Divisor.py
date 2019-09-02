"""https://www.interviewbit.com/problems/largest-coprime-divisor/

You are given two positive numbers A and B. You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1
For example,

A = 30
B = 12
We returnX = 5

"""
from math import sqrt, ceil
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        while(self.gcd(A, B) != 1):
            A = A//self.gcd(A, B)
        return A
                 
    def gcd(self, A, B):
        X= max(A, B)
        Y = min(A, B)
        while(Y > 0):
            X, Y = Y, X%Y    
        return X  
        
