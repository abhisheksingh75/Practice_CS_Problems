"""
Given an integer A representing the square blocks. The height of each square block is 1. The task is to create a staircase of max height using these blocks. The first stair would require only one block, the second stair would require two blocks and so on. Find and return the maximum height of the staircase. 
Input Format
The only argument given is integer A.
Output Format
Return the maximum height of the staircase using these blocks.
Constraints
0 <= A <= 10^9
For Example
Input 1:
    A = 10
Output 1:
    4

Input 2:
    A = 20
Output 2:
    5
   """
   class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        low = 0
        high = 10**5 
        while(high-low>1):
            mid = low + (high-low)//2
            #print("mid :"+str(mid)+"low :"+str(low)+"high :"+str(high))
            block_Req = (mid*(mid+1))//2    
            #print("block_Req"+str(block_Req))
            if block_Req <= A:
                low = mid
            else:
                high = mid
        return low
