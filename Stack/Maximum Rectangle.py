"""
Given a 2D binary matrix of integers A containing 0's and 1's of size N x M. Find the largest rectangle containing only 1's and return its area. Note: Rows are numbered from top to bottom and columns are numbered from left to right. 
Input Format
The only argument given is the integer matrix A.
Output Format
Return the area of the largest rectangle containing only 1's.
Constraints
1 <= N, M <= 1000
0 <= A[i] <= 1
For Example
Input 1:
    A = [   [0, 0, 1]
            [0, 1, 1]
            [1, 1, 1]   ]
Output 1:
    4

Input 2:
    A = [   [0, 1, 0, 1]
            [1, 0, 1, 0]    ]
Output 2:
"""
def calcArea(hist,stack,i):
    
    ele_indx = stack.pop()
    ele_height = hist[ele_indx]
    
    if stack == []:
        area = ele_height*i
    else:
        area = ele_height*(i-stack[-1]-1)
    
    return area


def histArea(hist):
    area, maxArea = 0, -1
    stack = []
    i =0
    
    while(i<len(hist)):
        
        if stack == [] or hist[stack[-1]]<=hist[i]:
            stack.append(i)
            i +=1
        else:
            area = calcArea(hist,stack,i)
            maxArea = max(maxArea,area)
            
    while(stack != []):
        area = calcArea(hist,stack,i)
        maxArea = max(maxArea,area)
    return maxArea
        
        


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        
        max_area = -1
        area = 0
        for i in range(len(A)):
            for j in range(len(A[0])): 
                if A[i][j] != 0 and i>0:
                    A[i][j] = A[i][j]+A[i-1][j]
            area = histArea(A[i])
            max_area = max(max_area,area)
            
        return max_area
