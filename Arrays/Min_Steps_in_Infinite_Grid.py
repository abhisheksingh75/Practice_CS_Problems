"""https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Input :

Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.
Output :

Return an Integer, i.e minimum number of steps.
Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

This question is intentionally left slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.
"""
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        distance_sum = 0
        for i in range(0, len(A)-1):
            distance_sum += self.two_points_distance(A[i], B[i], A[i+1], B[i+1]) 
    
        return distance_sum

    def two_points_distance(self, src_x, src_y, tgt_x, tgt_y):
        distance = 0  
        diff_row = abs(src_x - tgt_x)
        dif_colm = abs(src_y- tgt_y)
        return max(diff_row, dif_colm)
        """
        while(True):
            if diff_row <=0 and dif_colm <=0:
                return distance
            else:
                distance += 1 
                diff_row -= 1
                dif_colm -= 1
        """
       
