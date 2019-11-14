"""
Given two array of integers A and B describing a pair of (A[i], B[i]) coordinates in 2-D plane. A[i] describe x coordinates of the ith point in 2D plane whereas B[i] describes the y-coordinate of the ith point in 2D plane. Find and return the maximum number of points which lie on the same line. 
Input Format
The arguments given are integer arrays A and B.
Output Format
Return the maximum number of points which lie on the same line.
Constraints
1 <= (length of the array A = length of array B) <= 1000
-10^5 <= A[i], B[i] <= 10^5 
For Example
Input 1:
    A = [-1, 0, 1, 2, 3, 3]
    B = [1, 0, 1, 2, 3, 4]
Output 1:
    4
    The maximum number of point which lie on same line are 4, those points are {0, 0}, {1, 1}, {2, 2}, {3, 3}

Input 2:
    A = [3, 1, 4, 5, 7, -9, -8, 6]
    B = [4, -8, -3, -2, -1, 5, 7, -4]
Output 2:
    2
    """
    def calcSlope(x1,y1,x2,y2):
    x_diff = x2-x1
    y_diff = y2-y1
    com_base = gcd(abs(x_diff),abs(y_diff))
    if com_base != 0:
        x_diff,y_diff = x_diff//com_base,y_diff//com_base
        
    if y_diff == 0:
        return (0,1)
    elif x_diff< 0 and y_diff<0:
        return (abs(x_diff),abs(y_diff))
    elif x_diff< 0 or y_diff<0:
        return (-1*abs(x_diff),abs(y_diff))
    else:
        return (x_diff, y_diff)

def gcd(X,Y):
    X,Y = max(X,Y), min(X,Y)
    while(Y>0):
        X,Y = Y, X%Y
    return X
    
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        max_slope = 0
        for i in range(N): #cal curr_Slope wrt to each element of A[i]
            dic_slope = {}
            cur_slope,vertical_pt,overlap_pt = 0,0,0
            for j in range(i+1, N): #cal curr_slope wrt to each elemtent of A[i] relative to other points
                #if i == j:
                #    continue
                if A[i] == A[j]: # when x co-ordinate of two points equal
                    if B[i] == B[j]:# when y co-ordinate of two points equal
                       overlap_pt  += 1
                    else:
                        vertical_pt += 1
                else:
                    #calcualte slope
                    slope = calcSlope(A[i],B[i],A[j], B[j])
                    if slope in dic_slope:
                        dic_slope[slope] += 1
                    else:
                        dic_slope[slope] = 1
                    cur_slope = max(cur_slope, dic_slope[slope])
            cur_slope = max(cur_slope+overlap_pt+1, vertical_pt+overlap_pt+1)
            #print("i,j"+str(A[i])+","+str(B[i])+"cur_slope"+str(cur_slope)+"overlap_pt"+str(overlap_pt)+"vertical_pt"+str(vertical_pt)+"dic_slope"+str(dic_slope))
            max_slope = max(max_slope, cur_slope)
            #print("max_slope"+str(max_slope))
        
        return max_slope
                    
                    
                    
                    
                    
                    
                    
