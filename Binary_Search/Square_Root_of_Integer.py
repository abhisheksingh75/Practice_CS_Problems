"""
Implement int sqrt(int x). Compute and return the square root of x. If x is not a perfect square, return floor(sqrt(x)) Example :
Input : 11
Output : 3
"""
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        low = 0
        high = A
        square = 0
        if A == 1:
            return 1
        while(high-low>1):
            mid = low + (high-low)//2
            square = mid*mid
            if square == A:
                return mid
            elif square < A:
                low = mid 
            else:
                high = mid
        return low
                
            
            
