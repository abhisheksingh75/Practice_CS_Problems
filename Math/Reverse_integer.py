"""
Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer
"""
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        negative_flag = False
        B = 0
        if A < 0:
            A *= -1
            negative_flag = True
        while(A > 0):
            B = B*10 + (A%10)
            A = A//10
        if B > ((1<<31)-1):
            return 0
        else:
            if negative_flag is True:
                return B*-1
            else:
                return B
        
