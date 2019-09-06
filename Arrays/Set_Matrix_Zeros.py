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
        noOfRow = len(A)
        noOfCol  = len(A[0])
        rowflag, colflag = 1,1
        #check if 1st row is having zero's 
        for i in range(noOfCol):
            if A[0][i]  == 0:
                rowflag = 0
                break
            
        #check if 1st column is having zero's    
        for i in range(noOfRow):
            if A[i][0]  == 0:
                colflag = 0
                break
        
        #traverse the matrix and mark that row and column corresponding to element zero    
        for i in range(1, noOfRow,1):
            for j in range(1, noOfCol,1):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0
        
        #populate the matrix which having row and  column marked to zero
        for i in range(1, noOfRow,1):
            for j in range(1, noOfCol,1):
                if A[i][0] == 0 or A[0][j] == 0:
                    A[i][j] = 0
                    
                    
        #if rowflag is set mark whole row as zero
        if rowflag == 0:
            for i in range(noOfCol):
                A[0][i] = 0

        #if colflag is set mark whole row as zero
        if colflag == 0:
            for i in range(noOfRow):
                A[i][0] = 0
                    
        return A
                    
                    
                    
                    
                
                
     
