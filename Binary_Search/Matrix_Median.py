"""
Given a N cross M matrix in which each row is sorted, find the overall median of the matrix. Assume N*M is odd. For example,
Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

Median is 5. So, we return 5.
Note: No extra memory is allowed.
"""
from bisect import bisect_right    
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A): 
        no_of_rows = len(A)  
        no_of_colm = len(A[0])
        max_ele = A[0][0]
        min_ele = A[0][no_of_colm-1]
        
        desired_count = ((no_of_rows*no_of_colm)+1)//2
        
        for i in range(no_of_rows):
            min_ele =  min(A[i][0], min_ele)
            max_ele =  max(A[i][no_of_colm-1], max_ele)
       
        
        while(min_ele <  max_ele):
            count = 0 
            mid = (min_ele + max_ele)//2         
            for row in A:
                count += bisect_right(row, mid)
            if count < desired_count:
                min_ele = mid+1
            else:
               max_ele = mid 
            
        return min_ele
