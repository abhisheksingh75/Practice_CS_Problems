"""
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
     binary = bin(A)[2:].zfill(32)
     binary = binary[::-1]
     # converts reversed binary string into integer 
     return int(binary,2)
