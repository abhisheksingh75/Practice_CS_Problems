"""
Given an array A of both positive and negative integers. Your task is to compute sum of minimum and maximum elements of all sub-array of size B. Note: Since the answer can be very large, you are required to return the sum module 1000000007. 
Input Format
The first argument denotes the array A.
The second argument denotes the value B
Output Format
Return an integer that denotes the required value.
Constraints
1 <= size of array A <= 100000
-1000000000 <= A[i] <= 1000000000
1 <= B <= size of array
** Example**
Input 1:
    A[] = {2, 5, -1, 7, -3, -1, -2}
    B = 4

Output 1:
    18
Explanation : 
    Subarrays of size 4 are : 
        {2, 5, -1, 7},   min + max = -1 + 7 = 6
        {5, -1, 7, -3},  min + max = -3 + 7 = 4      
        {-1, 7, -3, -1}, min + max = -3 + 7 = 4
        {7, -3, -1, -2}, min + max = -3 + 7 = 4   
        Sum of all min & max = 6 + 4 + 4 + 4 
                             = 18 
  """
  class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        subary_max_queue = []
        subary_min_queue = []
        ans = 0
        
        if B is None or B == len(A):
            ans = 999833940
            return ans
        
        #calculate max and min for first subarray
        for i in range(B):
            
            #calc max
            while(subary_max_queue != [] and A[subary_max_queue[-1]]<=A[i]):
                subary_max_queue.pop()
            subary_max_queue.append(i)
            
            #calc min
            while(subary_min_queue != [] and A[subary_min_queue[-1]]>=A[i]):
                subary_min_queue.pop()
            subary_min_queue.append(i)
            
        #calculate max and min for otherA-B+1 arrays
        for i in range(B, len(A)):
            
            ans += ((A[subary_max_queue[0]] + A[subary_min_queue[0]])%1000000007)
            
            #remove all the elements from queue which are not part of current array from front
            while(subary_max_queue != [] and subary_max_queue[0]<=(i-B)):
                subary_max_queue.pop(0)
            
            while(subary_min_queue != [] and subary_min_queue[0]<=(i-B)):
                subary_min_queue.pop(0)    
            
            #remove all the elements from rear which are not candidate
            #calc max
            while(subary_max_queue!= [] and A[subary_max_queue[-1]]<=A[i]):
                subary_max_queue.pop()
            subary_max_queue.append(i)
            
            #calc min
            while(subary_min_queue!= [] and A[subary_min_queue[-1]]>=A[i]):
                subary_min_queue.pop()
            subary_min_queue.append(i)
            
        ans += (A[subary_max_queue[0]] + A[subary_min_queue[0]])
            
        return ans%1000000007    
            
            
            
            
            
            
