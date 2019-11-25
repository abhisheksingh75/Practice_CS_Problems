"""
Given an array of integers A of size N and an integer B. Find the first negative integer for each and every window(contiguous subarray) of size B. If a window does not contain a negative integer, then return 0 for that window. 
Input Format
The arguments given are integer array A and integer B.
Output Format
Return an integer array of size N+1-B representing answer of the ith window.
Constraints
1 <= length of the array <= 200000
-10^9 <= A[i] <= 10^9 
For Example
Input 1:
    A = [-1, 2, 3, -4, 5]
    B = 2
Output 1:
    [-1, 0, -4, -4] 

Input 2:
    A = [-8, 2, 3, -6, 10]
    B = 2
Output 2:
    [-8, 0, -6, -6]
    """
    class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):

        ans = []
        aux_queue = []
        
        #loop in first window 
        for i in range(B):
            if A[i]<0:
                aux_queue.append(i)
        
        for i in range(B, len(A)):
            
            if aux_queue!= []:
                ans.append(A[aux_queue[0]])
            else:
                ans.append(0)
            
            #remove the indexs which doesn't belong to this window
            while(aux_queue != [] and aux_queue[0]<=(i-B)):
                aux_queue.pop(0)
                
            if A[i]<0:
                aux_queue.append(i)
                
        if aux_queue!= []:
            ans.append(A[aux_queue[0]])
        else:
            ans.append(0)    
               
        return ans    
            
            
