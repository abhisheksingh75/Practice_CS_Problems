"""https://www.interviewbit.com/problems/set-matrix-zeros/
Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

Do it in place.

Example

Given array A as

1 0 1
1 1 1 
1 1 1
On returning, the array A should be :

0 0 0
1 0 1
1 0 1
"""
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        rowFlag,colFlag = 'N', 'N'
        noOfRow = len(A)
        noOfCol = len(A[0])
        
        #traverse first row
        for j in range(noOfCol):
            if A[0][j] == 0 or A[0][j] == 'Y': 
                A[0][j] = 'Y'            
                rowFlag = 'Y'
                
        #traverse first column
        for i in range(noOfRow):
            if A[i][0] == 0 or  A[i][0] == 'Y':
                A[i][0] = 'Y'
                colFlag = 'Y'
                
        
        for i in range(1, noOfRow):
            for j in range(1, noOfCol):
                if A[i][j] == 0:
                    A[i][0] = 'Y'
                    A[0][j] = 'Y'
        #start putting Zeros            
        for i in range(1, noOfRow):
            for j in range(1, noOfCol):
                if A[i][0] == 'Y' or A[0][j] == 'Y':
                   A[i][j] = 0
               
        #traverse first row
        for j in range(noOfCol):
            if rowFlag == 'Y' or A[0][j] == 'Y' :
                A[0][j] = 0
            
                
        #traverse first column
        for i in range(noOfRow):
            if colFlag == 'Y' or A[i][0] == 'Y':
                A[i][0] = 0
                
        return A
