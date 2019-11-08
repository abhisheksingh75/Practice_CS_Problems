"""Write a function that takes an unsigned integer and returns the number of 1 bits it has."""
import math 
class Solution:
    # @param A : integer
    # @return a strings
    def numSetBits(self, A):
        count  = 0
        while(A>0):            
            if str(A%2) == '1':
                count +=1
            A = int(math.floor(A>>1))            
        return count
