"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example: Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true ) Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem
"""
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        low = 0
        high = (len(A)*len(A[0]))-1
        no_of_col = len(A[0])
        
        while(low<=high):
            mid = low +(high-low)//2
            
            #calculate row , col corresponding to number
            row = mid//no_of_col
            col = mid%no_of_col
            
            if A[row][col] == B:
                return 1
            elif A[row][col] < B:
                low = mid + 1
            else:
                high = mid - 1
                
        return 0
