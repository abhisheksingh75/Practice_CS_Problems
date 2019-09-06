"""
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order. 
 Input Format:
The first and the only argument contains an integer, A.
Output Format:
Return a 2-d matrix of size A x A satisfying the spiral order.
Constraints:
1 <= A <= 1000
Examples:
Input 1:
    A = 3

Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]

Input 2:
    4

Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]
 """
 class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
            SpiralMatrix = [[0 for i in range(A)] for i in range(A)]
            maxRow, minRow = A-1, 0
            maxCol, minCol = A-1, 0
            ele = 1
            while(maxRow >= 0 and maxCol >= 0 and minRow <= A-1 and minCol <= A-1):
                
                "print left to right"
                for j in range(minCol, maxCol+1, 1):
                    SpiralMatrix[minRow][j] = ele
                    ele += 1
                minRow += 1
                
                "print top to bottom"
                for i in range(minRow,maxRow+1,1):
                    SpiralMatrix[i][maxCol] = ele
                    ele += 1
                maxCol -= 1
                
                "print right to left"
                for j in range(maxCol, minCol-1,-1):
                    SpiralMatrix[maxRow][j] = ele
                    ele += 1
                maxRow -= 1
                
                "print bottom to top"
                for i in range(maxRow,minRow-1, -1):
                    SpiralMatrix[i][minCol] = ele
                    ele += 1
                minCol += 1
            return SpiralMatrix
