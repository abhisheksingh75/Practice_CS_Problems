"""
You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees (clockwise). You need to do this in place. Note that if you end up using an additional array, you will only receive partial score. Example: If the array is
[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:
[
    [3, 1],
    [4, 2]
]
"""
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        N = len(A)-1
        
        for i in range(len(A)):
            for j in range(i, len(A)):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        
        for i in range(len(A)):
            count = 0
            while(count < len(A)//2):
                A[i][count],A[i][N-count] = A[i][N-count], A[i][count]
                count += 1
        return A
            
