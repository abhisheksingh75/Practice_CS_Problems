"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for a given array A of size N. If such arrangement is not possible, it must be rearranged as the lowest possible order i.e., sorted in an ascending order. Note:
1. The replacement must be in-place, do **not** allocate extra memory.
2. DO NOT USE LIBRARY FUNCTION FOR NEXT PERMUTATION. Use of Library functions will disqualify your submission retroactively and will give you penalty points.
Input Format:
The first and the only argument of input has an array of integers, A.
Output Format:
Return an array of integers, representing the next permutation of the given array.
Constraints:
1 <= N <= 5e5
1 <= A[i] <= 1e9
Examples:
Input 1:
    A = [1, 2, 3]

Output 1:
    [1, 3, 2]

Input 2:
    A = [3, 2, 1]

Output 2:
    [1, 2, 3]

Input 3:
    A = [1, 1, 5]

Output 3:
    [1, 5, 1]

Input 4:
    A = [20, 50, 113]

Output 4:
    [20, 113, 50]
    """
    class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        A =list(A)
        lenOfA = len(A)
        pos1 = -1
        for i in range(lenOfA-1, -1, -1):
            if A[i] > A[i-1]:
                pos1 = i-1
                break
        if pos1 == -1:
            return A[::-1]
        
        pos2 = pos1 + 1
        for i in range(pos2,lenOfA,1):
            if A[i] > A[pos1] and A[pos2] > A[i]:
                pos2 = i 
        
        A[pos1],A[pos2] = A[pos2], A[pos1]
        
        start = pos1+1
        end = len(A)-1
        while(start<end):
            A[start],A[end] = A[end], A[start]
            start += 1
            end -= 1
        
        return A
