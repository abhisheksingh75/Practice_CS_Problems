"""
Given an integer A. Find and Return first positive A integers in ascending order containing only digits 1,2 and 3. NOTE: all the A integers will fit in 32 bit integer. 
Input Format
The only argument given is integer A.
Output Format
Find and Return first positive A integers in ascending order containing only digits 1,2 and 3.
Constraints
1 <= A <= 29500
For Example
Input 1:
    A = 3
Output 1:
    [1, 2, 3]

Input 2:
    A = 7
Output 2:
    [1, 2, 3, 11, 12, 13, 21]
    """
    class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A): 
        
        queue = []
        queue.append(1)
        queue.append(2)
        queue.append(3)
        ans = []
        while((len(ans)+len(queue))<A):
            ele = queue.pop(0)
            queue.append((ele*10)+1)
            queue.append((ele*10)+2)
            queue.append((ele*10)+3)
            ans.append(ele)
        
        while(len(ans)<A):
            ele = queue.pop(0)
            ans.append(ele)
            
        return ans     
