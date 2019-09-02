"""https://www.interviewbit.com/problems/power-of-two-integers/

Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

Example

Input : 4
Output : True  
as 2^2 = 4. 
"""
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):   
        if A == 1:
            return 1           
        for x in range(2, int(math.floor(math.sqrt(A)))):
            y = 2 
            while(x**y <= A):
                if x**y == A:
                    return 1
                else:
                    y +=1                
        return 0    
    
